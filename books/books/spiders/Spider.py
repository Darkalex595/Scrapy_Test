import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = [
        'http://books.toscrape.com/'
        # 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html' 
    ]

    # def parse(self, response):
    #     for libros in response.css("article.product_pod"):
    #         yield {
    #             'titulo': libros.css("h3 a::attr(title)").get(),
    #             'precio': libros.css("div.product_price p.price_color::text").get(),
    #             'stock': libros.css("div.product_price p.instock.availability::text").get(),
    #             'image': libros.css("div.image_container a img.thumbnail::attr(src)").get() 
    #         }
    def parse(self, response):
        gen = response.css("article.product_pod")
        
        if gen != None:
            for libros in response.css("article.product_pod"):
                entrarLibro = libros.css("h3 a::attr(href)").get()
                entrarLibro = response.urljoin(entrarLibro)
                yield scrapy.Request(entrarLibro, callback=self.parse_detalles)
                
            sig_pag = response.css("ul.pager li.next a::attr(href)").get()
            if sig_pag:
                yield response.follow(sig_pag, callback = self.parse)
                
                
                
                
    def parse_detalles(self, response):
        
            cont = response.css("div.container-fluid.page")
            titulo = cont.css("div.page_inner div.content div#content_inner article.product_page div.row div.col-sm-6.product_main h1::text").get()
            categoria = cont.css("div.page_inner ul.breadcrumb li a::text").getall()
            categoria = categoria[2]
            cover = cont.css("div.page_inner div.content div#content_inner article.product_page div.row div.col-sm-6 div.carousel div.thumbnail div.carousel-inner div.item.active img::attr(src)").get()
            array = cont.css("div.page_inner div.content div#content_inner article.product_page table.table.table-striped td::text").getall()
            upc = array[0]
            tipo = array[1]
            precio = array[3]
            impuesto = array[4]
            disponibilidad = array[5]
            reviews = array[6]
            
            yield{
                'Titulo' : titulo,
                'Categoria' : categoria,
                'Cover' : cover,
                'UPC' : upc,
                'Tipo' : tipo,
                'Precio' : precio,
                'Impuesto' : impuesto,
                'Disponibilidad' : disponibilidad,
                'Reviews' : reviews
            }
            
            
            
    