# How to contribute
Thank you for showing interest in contributing to the plutopy package! Below you will find some guidelines that will get you contributing to this repository in no time!

## Getting Started
- Make sure you have a [GitHub account](https://github.com/signup/free)
- Make sure you have [Git](https://git-scm.com/downloads) installed
- Make sure you have [Anaconda](https://www.anaconda.com/download) installed
- Fork the repository on GitHub
- Clone the repository locally

## Set up a local plutopy environment

### Building the Anaconda Environment
Enter the cloned plutopy directory from the shell. Run the following command to build the required Anaconda environment.

```bash
conda env create -f environment.yml
```

Once the dependencies have been installed, you can activate the environment with `activate plutopy-env` on Windows, or `source activate plutopy-env` on mac / Linux. For more on Anaconda environments, see the documentation [here](https://conda.io/docs/using/envs.html).

### Installing plutopy locally
Make sure you are in the root plutopy directory and that the `plutopy-env` is activated. Run the following command to install a local version of plutopy:

```bash
pip install -e
```

This will allow you to `import plutopy` as long as the plutopy-env is activated.

### Keeping your fork up to date
As the main plutopy repository `cjtu/plutopy` is updated, your fork `<your_user>/plutopy` will get out of sync.

See [here](https://gist.github.com/CristinaSolana/1885435) for a quick guide on how to keep your fork up to date.

## Contributing
- Comment on the issue that you would like to work on, or open a new issue with your suggestion on the [issues](https://github.com/cjtu/plutopy/issues) page
- Start a new local git branch where you will develop your feature
- When your feature is ready, open a pull request from your feature branch to the plutopy master branch

## Code of Conduct
This repository is intended as an open and collaborative learning tool. It is governed by a code of conduct to make it safe and accessible for all. See the [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) for more details. 
