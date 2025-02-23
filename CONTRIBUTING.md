# Contribute

## Introduction

First, thank you for considering contributing to lesspass! It's people like you that make the open source community such a great community! 😊

We welcome any type of contribution, not only code. You can help with 
- **QA**: file bug reports, the more details you can give the better (e.g. screenshots with the console open)
- **Marketing**: writing blog posts, howto's, printing stickers, ...
- **Community**: presenting the project at meetups, organizing a dedicated meetup for the local community, ...
- **Code**: take a look at the [open issues](issues). Even if you can't write code, commenting on them, showing that you care about a given issue matters. It helps us triage them.
- **Money**: we welcome financial contributions in full transparency on our [open collective](https://opencollective.com/lesspass).

## Your First Contribution

Working on your first Pull Request? You can learn how from this *free* series, [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github).

## Development

### Tools

You'll need
 * nodejs
 * yarn

### Folder architecture

Here a some folders that worth noticing :
 * `package` contains the code for the web version and the browser extension. Development is done with `javascript` and `Vue`.
   * `lesspass-pure` contains the core of `lesspass`. Running `yarn dev` in this folder will run a `lesspass` instance locally.
   * `lesspass-web-extension` contains the code specific for the web extension.
   * `lesspass-render-password` contains the algorithm to generate passwords
 * `cli` contains the command line version. Development is done with `python`.
 * `mobile` contains the `android` and `ios` version. Development is done with `javascript` and `react native`.

### Commands

To install dependencies, please run `yarn install`

To run tests, you can run `yarn test` in the root directory or any sub-folder describe above.

## Submitting code

Any code change should be submitted as a pull request. The description should explain what the code does and give steps to execute it. The pull request should also contain tests.

## Code review process

The bigger the pull request, the longer it will take to review and merge. Try to break down large pull requests in smaller chunks that are easier to review and merge.
It is also always helpful to have some context for your pull request. What was the purpose? Why does it matter to you?

## Financial contributions

We also welcome financial contributions in full transparency on our [open collective](https://opencollective.com/lesspass).
Anyone can file an expense. If the expense makes sense for the development of the community, it will be "merged" in the ledger of our open collective by the core contributors and the person who filed the expense will be reimbursed.

## Questions

If you have any questions, create an [issue](issue) (protip: do a quick search first to see if someone else didn't ask the same question before!).
You can also reach us at contact@lesspass.com

## Credits

### Contributors

Thank you to all the people who have already contributed to lesspass!
<a href="graphs/contributors"><img src="https://opencollective.com/lesspass/contributors.svg?width=890" /></a>


### Backers

Thank you to all our backers! [[Become a backer](https://opencollective.com/lesspass#backer)]

<a href="https://opencollective.com/lesspass#backers" target="_blank"><img src="https://opencollective.com/lesspass/backers.svg?width=890"></a>


### Sponsors

Thank you to all our sponsors! (please ask your company to also support this open source project by [becoming a sponsor](https://opencollective.com/lesspass#sponsor))

<a href="https://opencollective.com/lesspass/sponsor/0/website" target="_blank"><img src="https://opencollective.com/lesspass/sponsor/0/avatar.svg"></a>
<a href="https://opencollective.com/lesspass/sponsor/1/website" target="_blank"><img src="https://opencollective.com/lesspass/sponsor/1/avatar.svg"></a>
<a href="https://opencollective.com/lesspass/sponsor/2/website" target="_blank"><img src="https://opencollective.com/lesspass/sponsor/2/avatar.svg"></a>
<a href="https://opencollective.com/lesspass/sponsor/3/website" target="_blank"><img src="https://opencollective.com/lesspass/sponsor/3/avatar.svg"></a>
<a href="https://opencollective.com/lesspass/sponsor/4/website" target="_blank"><img src="https://opencollective.com/lesspass/sponsor/4/avatar.svg"></a>
<a href="https://opencollective.com/lesspass/sponsor/5/website" target="_blank"><img src="https://opencollective.com/lesspass/sponsor/5/avatar.svg"></a>
<a href="https://opencollective.com/lesspass/sponsor/6/website" target="_blank"><img src="https://opencollective.com/lesspass/sponsor/6/avatar.svg"></a>
<a href="https://opencollective.com/lesspass/sponsor/7/website" target="_blank"><img src="https://opencollective.com/lesspass/sponsor/7/avatar.svg"></a>
<a href="https://opencollective.com/lesspass/sponsor/8/website" target="_blank"><img src="https://opencollective.com/lesspass/sponsor/8/avatar.svg"></a>
<a href="https://opencollective.com/lesspass/sponsor/9/website" target="_blank"><img src="https://opencollective.com/lesspass/sponsor/9/avatar.svg"></a>

<!-- This `CONTRIBUTING.md` is based on @nayafia's template https://github.com/nayafia/contributing-template -->
