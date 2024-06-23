import json
import graphviz
import sys


def load_workspace(file_path):
    # Загружаем JSON-файл
    with open(file_path, 'r') as file:
        return json.load(file)


def create_diagram(workspace):
    # Создаем новый граф
    dot = graphviz.Digraph(comment='Structurizr Workspace')

    # Добавляем элементы из рабочего окружения в граф
    for element in workspace.get('elements', []):
        dot.node(element['id'], element['name'])

    # Добавляем связи между элементами
    for relationship in workspace.get('relationships', []):
        dot.edge(relationship['sourceId'], relationship['destinationId'], label=relationship.get('description', ''))

    return dot


def save_diagram(diagram, output_path):
    # Сохраняем диаграмму в формате PNG
    diagram.render(output_path, format='png')


def main(input_file, output_file):
    # Загружаем рабочее окружение
    workspace = load_workspace(input_file)

    # Создаем диаграмму
    diagram = create_diagram(workspace)

    # Сохраняем диаграмму в PNG-файл
    save_diagram(diagram, output_file)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_json> <output_png>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    main(input_file, output_file)
