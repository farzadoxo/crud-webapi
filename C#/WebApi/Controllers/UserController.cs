using WebApi.Model;
using Microsoft.EntityFrameworkCore;
using Microsoft.Data.Sqlite;
using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Mvc;
using WebApi.DbContex;
using Microsoft.AspNetCore.Components;


namespace WebApi.Conteoller
{
    [Microsoft.AspNetCore.Components.Route("api/users")]
    [ApiController] 

    public class WebApiController : ControllerBase
    {
        private bool UserExists(int id)
        {
            return _context.Users.Any(e => e.Id == id);
        }
        private readonly WebApiContex _context;

        public WebApiController(WebApiContex context)
        {
            _context = context;
        }

        [HttpGet]
        public async Task<ActionResult<IEnumerable<User>>> GetAllUser()
        {
            return await _context.Users.ToListAsync();
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<User>> GetUserById(int id)
        {
            var user = await _context.Users.FindAsync(id);
            if  (user == null)
            {
                return NotFound();
            }
            else
            {
                return user;
            }
        }


        [HttpPost("")]
        public async Task<ActionResult<User>> AddUser(User user)
        {
            _context.Users.Add(user);
            await _context.SaveChangesAsync();
            return CreatedAtAction(nameof(GetUserById) , new{id = user.Id} , user);
        }

        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateUserInfo(int id , User user)
        {
            if(id != user.Id)
            {
                return BadRequest();
            }
            
            _context.Entry(user).State = EntityState.Modified;

            try{
                await _context.SaveChangesAsync();
            }
            catch(DbUpdateConcurrencyException){
                if(!UserExists(id))
                {
                    return NotFound();

                }
                throw;
            }
            return NoContent();
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteUser(int id)
        {
            var user = await _context.Users.FindAsync(id);
            if(user == null)
            {
                return NotFound();
            }

            _context.Users.Remove(user);
            await _context.SaveChangesAsync();

            return NoContent();

        }
        // private bool UserExists(int id)
        // {
        //     return _context.Users.Any(e => e.Id == id);
        // }

    }
}