
import os
import json
import shutil

current_dir = os.getcwd()
config_dir = os.path.join(current_dir, 'PROJECT_CREATOR_DATA')
project_name = input("Enter the name of the project: ")
template_name = input(
    "Enter the name of the template (from 'express', 'base'): ")
author_name = input("Enter the name of the author: ")


pkg_json = {
    "name": project_name,
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
        "start": "node dist/index.js",
        "debug": "nodemon src/index.ts",
    },
    "keywords": [],
    "author": author_name,
    "license": "ISC",
    "dependencies": {
        "config": "^3.3.6",
        "winston": "^3.3.3"
    },
    "devDependencies": {
        "@types/config": "^0.0.40",
        "@types/copy-webpack-plugin": "^8.0.1",
        "@types/webpack-node-externals": "^2.5.3",
        "copy-webpack-plugin": "^10.0.0",
        "ts-loader": "^9.2.6",
        "ts-node": "^10.4.0",
        "typescript": "^4.5.2",
        "webpack": "^5.64.2",
        "webpack-cli": "^4.9.1",
        "webpack-node-externals": "^3.0.0"
    }
}

ts_json = {
    "compilerOptions": {
        "target": "ES6",
        "module": "CommonJS",
        "rootDir": ".",
        "outDir": "dist",
        "esModuleInterop": True,
        "strict": True
    },
    "exclude": [
        "node_modules"
    ]
}
webpack_json = 'import path from"path";import webpack from"webpack";import nodeExternals from"webpack-node-externals";import TerserPlugin from"terser-webpack-plugin";import CopyPlugin from"copy-webpack-plugin";const config={entry:{server:"./src/index.ts"},watch:!1,target:"node",externals:[nodeExternals()],node:{__dirname:!1,__filename:!1},module:{rules:[{test:/\.ts$/,use:["ts-loader"],exclude:[/node_modules/]}]},mode:"development",resolve:{extensions:[".ts","tsx"]},plugins:[new webpack.HotModuleReplacementPlugin],optimization:{minimize:!0,minimizer:[new TerserPlugin({parallel:4,extractComments:!0,terserOptions:{sourceMap:!0}})]},output:{path:path.join(__dirname,"dist"),publicPath:"/",filename:"index.js"}};module.exports=config;'
default_config_json = json.dumps({
    'example_file': './txt/someFile.txt'
}, indent=4)


base_dir_struct = {
    'directories': {
        'src': {
            'directories': {
                'Controllers': {
                    'directories': {},
                    'files': {
                        'index': {
                            'ext': 'ts',
                            'copy': False,
                            'content': 'export { default as CConfiguration } from \'./CConfiguration\'\nexport { default as CFileSystem } from \'./CFileSystem\' '
                        },
                        'CConfiguration': {
                            'ext': 'ts',
                            'copy': False,
                            'content': "import { IConfiguration } from '../Interfaces'; \nimport config from 'config';\n\nexport default class CConfiguration implements IConfiguration { \n    checkIfExists = (name: string) => { \n        return config.has(name);\n    }\n    getConfiguration = <T>(configuration: string): T => { \n        return config.get(configuration) as T;\n    } \n    getConfigurationArray = <T>(prefix?: string, ...configurations: string[]): T[] => { \n        let local = prefix ? configurations.map((configuration) => `${prefix}.${configuration}`) : [...configurations]; \n        return local.map((configuration) => config.get(configuration));\n    }\n}"
                        },
                        'CFileSystem': {
                            'ext': 'ts',
                            'copy': False,
                            'content': "import { IFileSystem } from '../Interfaces';\n import fs from 'fs';\n import path from 'path';\n export default class CFileSystem implements IFileSystem {\n     readFile = (pathToFile: string) => {\n         return fs.readFileSync(pathToFile, { encoding: 'utf8' });\n     };\n     readFileArray = (pathsToFiles: string[]) => {\n         return pathsToFiles.map((filePath) => fs.readFileSync(filePath, { encoding: 'utf8' }));\n     };\n     readVaultFile = (pathToFile: string) => {\n         const currentConfigPath = process.env.NODE_CONFIG_DIR;\n         if (!currentConfigPath) throw new Error('No config path found!');\n         const completePath = path.join(currentConfigPath, pathToFile);\n         return fs.readFileSync(completePath, { encoding: 'utf8' });\n     };\n     readVaultFileArray = (pathsToFiles: string[]) => {\n         return pathsToFiles.map((filePath) => this.readVaultFile(filePath));\n     };\n }"

                        }
                    }
                },
                'Interfaces': {
                    'directories': {},
                    'files': {
                        'index': {
                            'ext': 'ts',
                            'copy': False,
                            'content': 'export { default as IConfiguration } from \'./IConfiguration\'\nexport { default as IFileSystem } from \'./IFileSystem\' '

                        },
                        'IConfiguration': {
                            'ext': 'ts',
                            'copy': False,
                            'content': "export default abstract class IConfiguration {\n    abstract getConfigurationArray<T>(prefix?: string, ...configurations: string[]): T[];\n    abstract getConfiguration<T>(name: string): T;\n    abstract checkIfExists(name: string): boolean;\n}\n"
                        },
                        'IFileSystem': {
                            'ext': 'ts',
                            'copy': False,
                            'content': "export default abstract class IFileSystem {\n    abstract readFile(pathToFile: string): string;\n    abstract readFileArray(pathsToFiles: string[]): string[];\n    abstract readVaultFile(pathToFile: string): string;\n    abstract readVaultFileArray(pathsToFiles: string[]): string[];\n}"
                        }
                    }
                },
                'config': {
                    'directories': {
                        'txt': {
                            'directories': {},
                            'files': {
                                'some_file': {
                                    'ext': 'txt',
                                    'copy': False,
                                    'content': 'Hello World!'
                                }
                            }
                        }
                    },
                    'files': {
                        'default': {
                            'ext': 'json',
                            'copy': False,
                            'content': default_config_json
                        },
                        'development': {
                            'ext': 'json',
                            'copy': False,
                            'content': default_config_json
                        },
                        'production': {
                            'ext': 'json',
                            'copy': False,
                            'content': default_config_json
                        }
                    }
                }
            },
            'files': {
                'index': {
                    'ext': 'ts',
                    'copy': False,
                    'content': "import path from 'path'\nprocess.env.NODE_CONFIG_DIR = path.join(__dirname, 'config')\n\n\n// Your code starts here!"
                }
            }

        }
    },
    'files': {
        'package': {
            'ext': 'json',
            'copy': False,
            'content': json.dumps(pkg_json, indent=4)
        },
        'tsconfig': {
            'ext': 'json',
            'copy': False,
            'content': json.dumps(ts_json, indent=4)
        },
        'webpack.config': {
            'ext': 'ts',
            'copy': False,
            'content': "import path from 'path'\nimport webpack from 'webpack'\nimport nodeExternals from 'webpack-node-externals'\nimport TerserPlugin from 'terser-webpack-plugin'\nimport CopyPlugin from 'copy-webpack-plugin'\nconst config = {\n    entry: {\n        server: './src/index.ts',\n    },\n    watch: false,\n    target: 'node',\n    externals: [nodeExternals()],\n    node: {\n        __dirname: false,\n        __filename: false,\n    },\n    module: {\n        rules: [{ test: /\.ts$/, use: ['ts-loader'], exclude: [/node_modules/] }],\n    },\n    mode: 'development',\n    resolve: {\n        extensions: ['.ts', 'tsx'],\n    },\n    plugins: [new webpack.HotModuleReplacementPlugin()],\n    optimization: {\n        minimize: true,\n        minimizer: [\n            new TerserPlugin({\n                parallel: 4,\n                extractComments: true,\n                terserOptions: {\n                    sourceMap: true,\n                },\n            }),\n        ],\n    },\n    output: {\n        path: path.join(__dirname, 'dist'),\n        publicPath: '/',\n        filename: 'index.js',\n    },\n};\nmodule.exports = config;\n"
        },
        'README': {
            'ext': 'md',
            'copy': False,
            'content': '# ' + project_name
        },
        '.gitignore': {
            'ext': '',
            'copy': False,
            'content': 'node_modules'
        }
    }
}


def check_if_directory_exists(directory):
    return os.path.isdir(directory)


if check_if_directory_exists(project_name):
    ask_delete = input('Directory ' + project_name +
                       ' already exists. Do you want to delete it? (y/n) ')
    if ask_delete == 'y':
        shutil.rmtree(project_name)
    else:
        print('Exiting...')
        exit()
os.mkdir(project_name)
# Move into the created directory
os.chdir(project_name)
# Tell the user we changed directories and moved into it
print('Created directory ' + project_name + ' and moved into it.')

# print the current directory
print('Current directory: ' + os.getcwd())

# Recursively create a directory tree


def copy_file(file_name, path):
    with open(file_name, 'r') as file:
        content = file.read()
    with open(path, 'w') as file:
        file.write(content)
    print(f'Copied file {os.path.join(os.getcwd(), path)}')


def create_directory_tree(directory_tree):
    for directory in directory_tree['directories']:
        os.mkdir(directory)
        print(f'Created {os.path.join(os.getcwd(), directory)}')
        os.chdir(directory)
        create_directory_tree(
            directory_tree['directories'][directory])
    for file in directory_tree['files']:
        curr_file = directory_tree['files'][file]
        if curr_file['copy']:
            copy_file(os.path.join(
                config_dir, curr_file['content']), file + '.' + curr_file['ext'])
        else:
            with open(file + '.' + curr_file['ext'], 'w') as f:
                f.write(curr_file['content'])
                print(f'Created file {file}.{curr_file["ext"]}')
    os.chdir('..')


create_directory_tree(base_dir_struct)

os.chdir(os.path.join(current_dir, project_name))
os.system('git init')
os.system('npm install')

print('Finished!')
