const url = "";

let produtos = [];
let categorias = [];

let produtoEditando = "";
let categoriaEditando = "";

const formProdutos = document.getElementById("form-produtos");
const formCategorias = document.getElementById("form-categorias");

function carregarCategorias() {
    return fetch(url + "/categorias/listar")
        .then(resposta => {
            if (!resposta.ok) throw new Error();
            return resposta.json();
        })
        .then(dados => {
            categorias = dados;
            listarCategorias();
            preencherCategorias();
        })
        .catch(() => alert("Erro ao carregar categorias."));
}

function carregarProdutos() {
    fetch(url + "/produtos/listar")
        .then(resposta => {
            if (!resposta.ok) throw new Error();
            return resposta.json();
        })
        .then(dados => {
            produtos = dados;
            listarProdutos();
        })
        .catch(() => alert("Erro ao carregar produtos."));
}

function listarCategorias(lista = categorias) {
    const tabela = document.getElementById("lista-categorias");
    if (!tabela) return;
    tabela.replaceChildren();

    lista.forEach(categoria => {
        const linha = tabela.insertRow();
        linha.insertCell().textContent = categoria.id;
        linha.insertCell().textContent = categoria.nome;

        const acoes = linha.insertCell();
        const botaoEditar = document.createElement("button");
        botaoEditar.textContent = "Editar";
        botaoEditar.onclick = () => {
            categoriaEditando = categoria.id;
            document.getElementById("nome").value = categoria.nome;
        };

        const botaoExcluir = document.createElement("button");
        botaoExcluir.textContent = "Excluir";
        botaoExcluir.onclick = () => excluirCategoria(categoria.id);
        acoes.append(botaoEditar, botaoExcluir);
    });

    if (!lista.length) tabela.innerHTML = '<tr><td colspan="3">Nenhuma categoria cadastrada.</td></tr>';
}

function listarProdutos(lista = produtos) {
    const tabela = document.getElementById("lista-produtos");
    if (!tabela) return;
    tabela.replaceChildren();

    lista.forEach(produto => {
        const linha = tabela.insertRow();
        const categoria = categorias.find(item => item.id === produto.categoria_id);
        linha.insertCell().textContent = produto.id;
        linha.insertCell().textContent = produto.nome;
        linha.insertCell().textContent = produto.preco;
        linha.insertCell().textContent = categoria ? categoria.nome : produto.categoria_id;

        const acoes = linha.insertCell();
        const botaoEditar = document.createElement("button");
        botaoEditar.textContent = "Editar";
        botaoEditar.onclick = () => {
            produtoEditando = produto.id;
            document.getElementById("nome").value = produto.nome;
            document.getElementById("preco").value = produto.preco;
            document.getElementById("categoria").value = produto.categoria_id;
        };

        const botaoExcluir = document.createElement("button");
        botaoExcluir.textContent = "Excluir";
        botaoExcluir.onclick = () => excluirProduto(produto.id);
        acoes.append(botaoEditar, botaoExcluir);
    });

    if (!lista.length) tabela.innerHTML = '<tr><td colspan="5">Nenhum produto cadastrado.</td></tr>';
}

function preencherCategorias() {
    const select = document.getElementById("categoria");
    if (!select) return;
    select.replaceChildren(new Option("Selecione uma categoria", ""));
    categorias.forEach(categoria => select.add(new Option(categoria.nome, categoria.id)));
}

function buscarCategoria() {
    const termo = document.getElementById("busca-categoria").value.toLowerCase();
    listarCategorias(categorias.filter(categoria =>
        String(categoria.id) === termo || categoria.nome.toLowerCase().includes(termo)
    ));
}

function buscarProduto() {
    const termo = document.getElementById("busca-produto").value.toLowerCase();
    listarProdutos(produtos.filter(produto =>
        String(produto.id) === termo || produto.nome.toLowerCase().includes(termo)
    ));
}

function excluirCategoria(id) {
    if (!confirm("Deseja excluir esta categoria?")) return;
    fetch(url + "/categorias/excluir/" + id, { method: "DELETE" })
        .then(resposta => {
            if (!resposta.ok) throw new Error();
            carregarCategorias();
        })
        .catch(() => alert("Não foi possível excluir a categoria."));
}

function excluirProduto(id) {
    if (!confirm("Deseja excluir este produto?")) return;
    fetch(url + "/produtos/excluir/" + id, { method: "DELETE" })
        .then(resposta => {
            if (!resposta.ok) throw new Error();
            carregarProdutos();
        })
        .catch(() => alert("Erro ao excluir produto."));
}

if (formCategorias) {
    formCategorias.onsubmit = event => {
        event.preventDefault();
        const categoria = { nome: document.getElementById("nome").value };
        const urlRota = categoriaEditando
            ? "/categorias/atualizar/" + categoriaEditando
            : "/categorias/cadastrar";

        fetch(url + urlRota, {
            method: categoriaEditando ? "PATCH" : "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(categoria)
        })
            .then(resposta => {
                if (!resposta.ok) throw new Error();
                categoriaEditando = "";
                formCategorias.reset();
                carregarCategorias();
            })
            .catch(() => alert("Erro ao salvar categoria."));
    };
}

if (formProdutos) {
    formProdutos.onsubmit = event => {
        event.preventDefault();
        const produto = {
            nome: document.getElementById("nome").value,
            preco: Number(document.getElementById("preco").value),
            categoria_id: Number(document.getElementById("categoria").value)
        };
        const urlRota = produtoEditando
            ? "/produtos/atualizar/" + produtoEditando
            : "/produtos/cadastrar";

        fetch(url + urlRota, {
            method: produtoEditando ? "PATCH" : "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(produto)
        })
            .then(resposta => {
                if (!resposta.ok) throw new Error();
                produtoEditando = "";
                formProdutos.reset();
                carregarProdutos();
            })
            .catch(() => alert("Erro ao salvar produto."));
    };
}

if (document.getElementById("lista-categorias")) carregarCategorias();
if (document.getElementById("lista-produtos")) {
    carregarCategorias().then(carregarProdutos);
}
