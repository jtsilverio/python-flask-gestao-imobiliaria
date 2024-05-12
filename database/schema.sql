CREATE TABLE IF NOT EXISTS `locatario` (
	`id` integer primary key NOT NULL UNIQUE,
	`cpf` TEXT NOT NULL,
	`primeiro_nome` TEXT NOT NULL,
	`ultimo_nome` TEXT NOT NULL,
	`email` TEXT NOT NULL,
	`ddd` INTEGER NOT NULL,
	`telefone` TEXT NOT NULL,
	`cep` TEXT NOT NULL,
	`logradouro` TEXT NOT NULL,
	`numero` TEXT NOT NULL,
	`complemento` TEXT,
	`bairro` TEXT NOT NULL,
	`cidade` INTEGER NOT NULL,
	`uf` INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `imovel` (
	`id` integer primary key NOT NULL UNIQUE,
	`cep` TEXT NOT NULL,
	`logradouro` TEXT NOT NULL,
	`numero` TEXT NOT NULL,
	`complemento` TEXT,
	`bairro` TEXT NOT NULL,
	`cidade` INTEGER NOT NULL,
	`uf` INTEGER NOT NULL,
	`alugado` TEXT NOT NULL,
	`id_locador` INTEGER NOT NULL,
	FOREIGN KEY(`id_locador`) REFERENCES `locador`(`id`)
);

CREATE TABLE IF NOT EXISTS `contrato` (
	`id` integer primary key NOT NULL UNIQUE,
	`data_inicio` REAL NOT NULL,
	`data_fim` REAL NOT NULL,
	`valor_aluguel` REAL NOT NULL,
	`IPTU` REAL NOT NULL,
	`condominio` REAL DEFAULT 0,
	`garantia` REAL DEFAULT 0,
	`outras_despesas` REAL DEFAULT 0,
	`porcentagem_comissao` REAL DEFAULT 0,
	`id_locatario` INTEGER NOT NULL,
	`id_imovel` INTEGER NOT NULL,
	FOREIGN KEY(`id_locatario`) REFERENCES `locatario`(`id`),
	FOREIGN KEY(`id_imovel`) REFERENCES `imovel`(`id`)
);

CREATE TABLE IF NOT EXISTS `locador` (
	`id` integer primary key NOT NULL UNIQUE,
	`cpf` TEXT NOT NULL,
	`primeiro_nome` TEXT NOT NULL,
	`ultimo_nome` TEXT NOT NULL,
	`email` TEXT NOT NULL,
	`ddd` INTEGER NOT NULL,
	`telefone` TEXT NOT NULL,
	`cep` TEXT NOT NULL,
	`logradouro` TEXT NOT NULL,
	`numero` TEXT NOT NULL,
	`complemento` TEXT,
	`bairro` TEXT NOT NULL,
	`cidade` INTEGER NOT NULL,
	`uf` INTEGER NOT NULL
);