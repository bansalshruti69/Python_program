import media
import tomatoes
jab=media.Movie("Jab Harry Met Sejal","Flop movie","http://s3.india.com/wp-content/uploads/2017/06/Jab-Harry-Met-Sejal-1.jpg","https://www.youtube.com/watch?v=v3WVAoaA0E0")
raees=media.Movie("Raees","Dhande se bada koi dharm nhi","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYwtcBE5btMqILDluKTEo4t6h0izqI6RaRdPbCyruFXUiwAOfItTdAgNM","https://www.youtube.com/watch?v=J7_1MU3gDk0")
ddlj=media.Movie("Dil waale dulhaniya le jayenge","A love story","https://s-media-cache-ak0.pinimg.com/564x/66/44/a3/6644a3ccd302490471890b27fbbe9d95.jpg","https://www.youtube.com/watch?v=c25GKl5VNeY")
tubelight=media.Movie("TubeLight","A flop movie","http://static.koimoi.com/wp-content/new-galleries/2017/04/tubelight-poster-2-salman-khan-shoes-dangling-around-neck-1.jpg","https://www.youtube.com/watch?v=PGQRNKHJwH4")
gf=media.Movie("Half Girlfriend","A Novel by Chetan Bhagat","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTC1va98lPzLNY8N49HlG_EaplPwl9O75misdqFpR_NIA6c6OxXYkyjQw","https://www.youtube.com/watch?v=KmlBnmyelHI")
baby=media.Movie("Baby","A movie by akshay kumar","http://www.gigareel.com/wp-content/uploads/2015/12/baby-movie-poster.jpg","https://www.youtube.com/watch?v=-Yu_2nyOP5o")
movies=[jab, raees, ddlj, tubelight, gf, baby]
tomatoes.open_movies_page(movies)
                
