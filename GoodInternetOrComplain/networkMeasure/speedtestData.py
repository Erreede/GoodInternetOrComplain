import speedtest

def performTest():
    try:
        try:
            s = speedtest.Speedtest(secure=True)
        except:
            s = speedtest.Speedtest()
        s.download()
        s.upload(pre_allocate=False)
        results = s.results.dict()
        results['png_url'] = s.results.share()
        return results
    except Exception as err:        
        print(f'Error occurred: {err}')
        return {}