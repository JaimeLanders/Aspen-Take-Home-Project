'use strict';

// start the web server
const app = require('../src');

const { expect } = require('chai');
const fetch = require('node-fetch');

describe('main endpoint', function() {
    const url = `http://localhost:${app.locals.PORT}`;

    it('returns default "Hello world!"', function() {
        return fetch(url)
            .then(res => res.json())
            .then(json => {
                expect(json.msg).to.eql('Hello world!');
            })
    });
});
