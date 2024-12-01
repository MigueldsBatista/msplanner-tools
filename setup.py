from setuptools import setup, find_packages
# Lê o README.md como descrição longa
long_description = (
    open("README.md").read()
)
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="msplanner-tools",
    version="0.1.8",
    description="Library to interact with Microsoft Planner via API Graph",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Miguel Batista",
    author_email="miguelsbatista0610@gmail.com",
    license="MIT",  # Ajuste de acordo com sua licença
    python_requires=">=3.7",
    packages=find_packages(),  # Busca automaticamente os pacotes no diretório
    install_requires=[
        "requests",
        "msal",
    ],
    include_package_data=True,  # Inclui arquivos não-Python especificados no MANIFEST.in
    keywords=["Microsoft Planner", "API", "Graph", "Python", "Tasks", "Buckets", "Plans"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/MigueldsBatista/msplanner-tools",  # Adicione esta linha
    project_urls={
        "Repository": "https://github.com/MigueldsBatista/msplanner-tools",
        "Documentation": "https://github.com/MigueldsBatista/msplanner-tools#readme",
    },
)

