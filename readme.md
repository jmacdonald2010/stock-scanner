# Stock Scanner

## Description

This project is meant to make my life a little bit easier by automating part of the stock research process, by fetching data daily on various stocks, storing them in a database, and making it easy to perform analyses to see how various fundamentals and other data points have changed over time. 

This is very much still a work in progress. The MVP will run after market close, fetch the new data, and store it. Future iterations of this project will include a script to automatically send emails with important updates on my holdings and stocks that may be worth keeping a closer eye on. I also hope to build a dashboard (using Dash) that can be run locally. 

The notebooks are mostly for sketching out ideas or trying features of packages I haven't used before.

The plan is to deploy the project to a Raspberry Pi in my home.

## Roadmap

- Complete database writing functions.
- Write automated script to fetch data, store data.
- Deploy script and database as containers (using docker) on a Raspberry Pi in my home.
- Collect some data.
- Build a basic recommendation email template to send to myself, showing how my holdings are doing and if any other stocks are worth looking into.
- Build a Dashboard to easily be able to visualize any datapoint on any given symbol.

## Contributing

This is mostly a solo project intended to automate part of my life, but if you have some suggestions/recommendations, feel free to make a pull request.

## License: MIT License.

## Project Status
Work in progress, not functional. Early development stages.