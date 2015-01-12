var casper = require('casper').create({
    verbose: true,
        logLevel: "debug"
        });

/*
function getElementByXpath (path) {
    this.evaluate(function(){
        return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
  })
}
*/


//require("utils").dump(casper.cli.args);
var xPaths
var resultsobject = {}
var startURL = 'http://public.leginfo.state.ny.us/LAWSSEAF.cgi?QUERYTYPE=LAWS+&QUERYDATA=@LLVAT+&LIST=LAW+&BROWSER=BROWSER+&TOKEN=50805005+&TARGET=VIEW'

if (casper.cli.args.length > 0){
    startURL = casper.cli.args[0]
}
//console.log(casper.cli.args.length)
/*
for (arg in casper.cli.args){
    console.log(arg)
}
*/

x = require('casper').selectXPath;
console.log('startURL',startURL)

//casper.exit()


casper.start(startURL);

casper.then(function getLinks(){
    //xPaths = this.evaluate(function(){
    resultsobject = this.evaluate(function(){
        // copied from http://stackoverflow.com/a/5178132/1816580
        function createXPathFromElement(elm) {
            var allNodes = document.getElementsByTagName('*'); 
            for (var segs = []; elm && elm.nodeType == 1; elm = elm.parentNode) { 
                if (elm.hasAttribute('id')) { 
                        var uniqueIdCount = 0; 
                        for (var n=0;n < allNodes.length;n++) { 
                            if (allNodes[n].hasAttribute('id') && allNodes[n].id == elm.id) uniqueIdCount++; 
                            if (uniqueIdCount > 1) break; 
                        }; 
                        if ( uniqueIdCount == 1) { 
                            segs.unshift('id("' + elm.getAttribute('id') + '")'); 
                            return segs.join('/'); 
                        } else { 
                            segs.unshift(elm.localName.toLowerCase() + '[@id="' + elm.getAttribute('id') + '"]'); 
                        } 
                } else if (elm.hasAttribute('class')) { 
                    segs.unshift(elm.localName.toLowerCase() + '[@class="' + elm.getAttribute('class') + '"]'); 
                } else { 
                    for (i = 1, sib = elm.previousSibling; sib; sib = sib.previousSibling) { 
                        if (sib.localName == elm.localName)  i++; }; 
                        segs.unshift(elm.localName.toLowerCase() + '[' + i + ']'); 
                }; 
            }; 
            return segs.length ? '/' + segs.join('/') : null; 
        };
        var links = document.getElementsByTagName('a');
        /*
        for (link in links){
            this.echo('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX' + link.innerHTML)
        }
        */
        var xPaths = Array.prototype.map.call(links, createXPathFromElement);
        //return xPaths;
        return {'xPaths': xPaths, 'links': links}

    });
});
casper.then(function(){
    var currentTime = new Date();
    var month = currentTime.getMonth() + 1;
    var day = currentTime.getDate();
    var year = currentTime.getFullYear();
    var myfile1 = "data-"+year + "-" + month + "-" + day+"_links.log.txt";
    var fs1 = require('fs');
    var laws = []
    //this.each(xPaths, function(self, xpath){

    this.echo('QQQQ: ' + JSON.stringify(resultsobject.links))
    fs1.write('links.json', JSON.stringify(resultsobject.links,null,4), 'w')

    /*
    this.each(resultsobject.links, function(self, link){
            this.echo('QQQQQQQ: '+this.link);
    })
    */
    this.each(resultsobject.xPaths, function(self, xpath){
        self.thenOpen(startURL);
        self.thenClick(x(xpath));
        // waiting some time may be necessary for single page applications
        self.wait(1000);
        self.then(function(a){
            // do something meaningful here
            this.echo(this.getCurrentUrl());
            fs1.write(myfile1, this.getCurrentUrl()+'\n', 'w+');
            //fs1.write(myfile1, 'xpath:'+ xpath + ' a: '+ JSON.stringify(a) + '\n', 'w+');
            //fs1.write(myfile1, 'xpath:'+ x(xpath) + '\n', 'w+');

            //fs1.write(myfile1, 'xpath:'+ document.getElementByXpath(xpath).innerHTML + '\n', 'w+');
            //fs1.write(myfile1, 'xpath:'+ getElementByXpath(xpath).innerHTML + '\n', 'w+');

            require('utils').dump((this.getPageContent()))
            var currentTime = new Date();
            var month = currentTime.getMonth() + 1;
            var day = currentTime.getDate();
            var year = currentTime.getFullYear();
            //var myfile = "law/data-"+year + "-" + month + "-" + day+"_"+this.getCurrentUrl().replace(/[:\/@+&]/g,'_')+".html";
            var myfile = "law/data-"+year + "-" + month + "-" + day+"_"+escape(this.getCurrentUrl().replace(/\//g,'_'))+".html";
            var fs = require('fs');
            fs.write(myfile, this.getPageContent(), 'w');
            //laws.push({'link':escape(this.getCurrentUrl().replace(/\//g,'_')), 'content': this.getPageContent()})
            //object1=({'link':escape(this.getCurrentUrl().replace(/\//g,'_')), 'content': this.getPageContent()})
            object1=({'link':escape(this.getCurrentUrl().replace(/\//g,'_')), 'content': this.getPageContent().replace(/<\/?[^>]+(>|$)/g, "")})
            //fs1.write('laws.json', JSON.stringify(laws,null,4), 'w')
            fs1.write('laws.json', JSON.stringify(object1)+ '\n', 'a+')

        });
    });
});
casper.run(function(){
    this.exit();
});
