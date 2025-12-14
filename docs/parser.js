// parser.js
const { parse } = require('json5');

class Parser {
  async parseFile(filePath) {
    try {
      const fileContent = await this.readFile(filePath);
      return parse(fileContent);
    } catch (error) {
      throw new Error(`Error parsing file: ${error.message}`);
    }
  }

  async readFile(filePath) {
    try {
      return await Deno.readTextFile(filePath);
    } catch (error) {
      throw new Error(`Error reading file: ${error.message}`);
    }
  }
}

module.exports = Parser;