using System;
using Discord.Commands;


namespace ScuttleClasses
{
    
    public class InfoModule : ModuleBase<SocketCommandContext>
    {
        // !say hello world -> hello world
        [Command("hi")]
        [Summary("Echos a message")]
        public async Task SayAsync()
        {
            await Context.Channel.SendMessageAsync("Hello there!");
        }

    }
}
