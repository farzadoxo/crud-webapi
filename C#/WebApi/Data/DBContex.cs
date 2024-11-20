using WebApi.Model;
using Microsoft.EntityFrameworkCore;
using Microsoft.Data.Sqlite;


namespace WebApi.DbContex
{

    public class WebApiContex : DbContext
    {
        string sqliteConnectionPath = "DataBase.db;Version=3";
        public WebApiContex(DbContextOptions<WebApiContex> options) : base(options) {}

        public DbSet<User> Users {get; set;}

    }
    
}

