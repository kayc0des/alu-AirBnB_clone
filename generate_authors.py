#Python File to Generate Authors

#List of dicts containing authors
authors = [
    {
        'name': 'Kingsley B. Boafo',
        'email': 'k.boafo@alustudent.com',
        'github': 'kayc0des',
        'role': 'SE Student'
    },
    {
        'name': 'Davis Gatabazi',
        'email': 'd.gatabazi@alustudent.com',
        'github': 'therealgatabazi',
        'role': 'SE Student'
    },
]
#function to generate the Markdown file content based on the authors' information
def generate_authors_file(authors):
    content = '# Authors\n\n'
    
    for author in authors:
        github_link = f'https://github.com/{author["github"]}'
        content += f'- [{author["name"]}]( {github_link} ) - {author["role"]}\n'

    return content

#Call the generate_authors_file() function with the authors list and write the output to a file
output_file = 'AUTHORS.md' 

with open(output_file, 'w') as file:
    file.write(generate_authors_file(authors))