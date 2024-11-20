namespace WebApi.Model
{
    public class BasicInfo
    {
        public int Id {get; set;}
        public string? Name {get; set;}
        public int Age {get; set;}

    }

    public class User : BasicInfo
    {
        public string? UserName {get; set;}
        public string? Password {get; set;}
    }
}


