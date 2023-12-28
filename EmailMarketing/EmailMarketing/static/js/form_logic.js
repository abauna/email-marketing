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










document.addEventListener('DOMContentLoaded', function() {
    const tabelaDisponibilidade = document.getElementById('tabela-disponibilidade');
    const diasSemana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb']; // Siglas dos dias da semana

    const disponibilidade = {
        Seg: Array(13).fill(1), // Define todos os horários de Segunda como ocupados inicialmente
        Ter: Array(13).fill(1), // Define todos os horários de Terça como ocupados inicialmente
        Qua: Array(13).fill(1), // Define todos os horários de Quarta como ocupados inicialmente
        Qui: Array(13).fill(1), // Define todos os horários de Quinta como ocupados inicialmente
        Sex: Array(13).fill(1), // Define todos os horários de Sexta como ocupados inicialmente
        Sáb: Array(13).fill(1), // Define todos os horários de Sábado como ocupados inicialmente
    };

    for (let hora = 8; hora <= 20; hora++) {
        const linhaHorario = document.createElement('tr');
        const tdHorario = document.createElement('td');
        tdHorario.textContent = `${hora.toString().padStart(2, '0')}:00`;
        linhaHorario.appendChild(tdHorario);

        for (const dia of diasSemana) {
            const tdDia = document.createElement('td');
            tdDia.dataset.dia = dia.toLowerCase();
            tdDia.dataset.hora = `${hora.toString().padStart(2, '0')}:00`;
            tdDia.classList.add('horario-disponivel');
            tdDia.classList.add('ocupado'); // Todos os horários começam como ocupados
            linhaHorario.appendChild(tdDia);
        }

        tabelaDisponibilidade.appendChild(linhaHorario);
    }

    const horarios = document.querySelectorAll('.horario-disponivel');
    horarios.forEach(function(horario) {
        horario.addEventListener('click', function() {
            if (this.classList.contains('ocupado')) {
                this.classList.remove('ocupado');
                this.classList.add('disponivel');
            } else if (this.classList.contains('disponivel')) {
                this.classList.remove('disponivel');
                this.classList.add('ocupado');
            }

            // Atualiza o objeto disponibilidade com os dados da tabela
            const dia = this.dataset.dia.charAt(0).toUpperCase() + this.dataset.dia.slice(1); // Converte a primeira letra para maiúscula
            const horaIndex = parseInt(this.dataset.hora.substring(0, 2)) - 8; // Obtém o índice baseado na hora (8am começa no índice 0)
            disponibilidade[dia][horaIndex] = this.classList.contains('ocupado') ? 1 : 0;
            
            // Atualiza o valor do campo 'disponibilidade'
            const disponibilidadeInput = document.getElementById('id_disponibilidade');
            disponibilidadeInput.value = JSON.stringify(disponibilidade);
        });
    });
});
