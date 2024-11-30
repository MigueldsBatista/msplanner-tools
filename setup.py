from setuptools import setup, find_packages

setup(
    name="msplanner-tools",
    version="0.1.6",
    description="Library to interact with Microsoft Planner via API Graph",
    long_description=open("README.md").read(),
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
    keywords=["Microsoft Planner", "API", "Graph", "Python", "Tasks", "Buckets", "Plans"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Repository": "https://github.com/MigueldsBatista/msplanner-tools",
    },
)

