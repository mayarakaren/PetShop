/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Copiando estrutura do banco de dados para escola
DROP DATABASE IF EXISTS `petshop`;
CREATE DATABASE IF NOT EXISTS `petshop` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `petshop`;

-- Copiando estrutura para tabela escola.aluno
CREATE TABLE IF NOT EXISTS `User` (
  `codigo` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(250) DEFAULT NULL,
  `senha` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

ALTER TABLE imagem ADD COLUMN idImg int(11) NOT NULL;

CREATE TABLE IF NOT EXISTS `Clientes` (
  `codigo` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(250) DEFAULT NULL,
  `idade` varchar(3) DEFAULT NULL,
  `sexo` varchar(1) DEFAULT NULL,
  `celular` varchar(11) DEFAULT NULL,
  `endereco` varchar(250) DEFAULT NULL,
  `cpf` varchar(11) DEFAULT NULL,
  `data` varchar(10) DEFAULT NULL,
  `cadastro` varchar(10) DEFAULT NULL,
  `bairro` varchar(250) DEFAULT NULL,
  `cidade` varchar(250) DEFAULT NULL,
  `estado` varchar(250) DEFAULT NULL,
  `descricao` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

create table imgCliente (
`imagem_cliente` blob DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS `Animais` (
  `codigo` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(250) DEFAULT NULL,
  `idade` varchar(3) DEFAULT NULL,
  `sexo` varchar(1) DEFAULT NULL,
  `raca` varchar(250) DEFAULT NULL,
  `peso` varchar(5) DEFAULT NULL,
  `especie` varchar(250) DEFAULT NULL,
  `data` varchar(10) DEFAULT NULL,
  `cadastro` varchar(10) DEFAULT NULL,
  `atualizacao` varchar(10) DEFAULT NULL,
  `descricao` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

create table imgAnimal (
`imagem_animal` blob DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS `Servico` (
  `codigo` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(250) DEFAULT NULL,
  `tipo` varchar(250) DEFAULT NULL,
  `valor` varchar(8) DEFAULT NULL,
  `tempo` varchar(250) DEFAULT NULL,
  `descricao` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

create table imagem (
`imagem_servico` blob DEFAULT NULL
);

select * from Clientes;
select * from Animais;
select * from Servico;
select * from imagem;
select * from imgCliente;
select * from imgAnimal;

drop table imgCliente;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;