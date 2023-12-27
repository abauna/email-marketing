// form_logic.js

$(document).ready(function () {
    $('#id_curso').change(function () {
        var cursoSelecionado = $(this).val();
        var professoresSelect = $('#id_professor');
        var conteudoSelect = $('#id_conteudo');

        professoresSelect.empty();
        conteudoSelect.empty();

        if (cursoSelecionado === 'curso1') {
            professoresSelect.append('<option value="andre">Andre</option>');
            professoresSelect.append('<option value="natalia">Natalia</option>');

            // Preenche o conteúdo para o curso 1
            conteudoSelect.append('<option value="conteudo1">Conteúdo do Curso de Inglês</option>');
            conteudoSelect.append('<option value="conteudo2">Outro Conteúdo do Curso de Inglês</option>');
        } else if (cursoSelecionado === 'curso2') {
            professoresSelect.append('<option value="leandro">Leandro</option>');
            professoresSelect.append('<option value="vanderlei">Vanderlei</option>');
            professoresSelect.append('<option value="jackson">Jackson</option>');

            // Preenche o conteúdo para o curso 2
            conteudoSelect.append('<option value="conteudo3">Conteúdo do Curso de Informática</option>');
            conteudoSelect.append('<option value="conteudo4">Outro Conteúdo do Curso de Informática</option>');
        }
    });
});
