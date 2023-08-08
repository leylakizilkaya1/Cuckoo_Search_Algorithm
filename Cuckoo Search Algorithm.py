#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
import numpy as np

# Optimize edilecek fonksiyon (örnek olarak Rosenbrock fonksiyonu)
def objective_function(x):
    return sum(100.0 * (x[1:] - x[:-1]**2.0)**2.0 + (1 - x[:-1])**2.0)

#Kodun başında, gerekli kütüphaneleri (numpy ve random) içe aktarıyoruz.
#objective_function adında bir fonksiyon tanımlıyoruz. Bu, optimize edilmeye çalışan bir fonksiyonu temsil eder.
#Örnek olarak Rosenbrock fonksiyonunu kullanıyoruz.


# Guguk Kuşu Algoritması
def cuckoo_search(objective, dimensions, population_size, generations):
    lower_bound = -5.0
    upper_bound = 5.0
    
    best_solution = None
    best_fitness = float('inf')
    
    # Başlangıç populasyonu oluştur
    population = np.random.uniform(lower_bound, upper_bound, (population_size, dimensions))
    
#cuckoo_search adında Guguk Kuşu Algoritması'nı uygulayan bir fonksiyon tanımlıyoruz.
#Bu fonksiyon, optimize edilecek fonksiyonu (objective), çözümlerin boyutunu (dimensions), populasyon boyutunu (population_size)
#ve iterasyon sayısını (generations) parametre olarak alır.

#lower_bound ve upper_bound değişkenleri, çözümlerin aralığını belirtir.
#best_solution ve best_fitness değişkenleri, en iyi çözümü ve bu çözümün fitness değerini saklamak için kullanılır.
#Başlangıç populasyonunu np.random.uniform fonksiyonu ile oluşturuyoruz.
    
    
    for gen in range(generations):
        population_fitness = [objective(sol) for sol in population]  # Her çözümün fitness değerini hesapla
        
        for i in range(population_size):
            # Yeni çözüm yarat
            new_solution = population[i] + np.random.normal(0, 1, dimensions)
            new_solution = np.clip(new_solution, lower_bound, upper_bound)
            
            # Yeni çözümün fitness değerini hesapla
            new_fitness = objective(new_solution)
            
            # Yeni çözümü kabul edip etmeme kararını ver
            if new_fitness < population_fitness[i]:
                population[i] = new_solution
                population_fitness[i] = new_fitness  # Fitness değerini güncelle
                if new_fitness < best_fitness:
                    best_fitness = new_fitness
                    best_solution = new_solution
                    
#Algoritma, belirtilen iterasyon sayısı boyunca çalışır.
#Her iterasyonda, populasyonun fitness değerlerini hesaplıyoruz.
#Her bir çözüm için yeni bir çözüm oluşturuyoruz. Bu yeni çözüm, normal dağılıma göre rasgele bir değer ekleyerek elde edilir.
#Yeni çözümün değerlerini aralığa sığdırmak için np.clip fonksiyonunu kullanıyoruz.
#Yeni çözümün fitness değerini hesaplayıp mevcut çözüm ile karşılaştırarak kabul edip etmeyeceğimize karar veriyoruz.
#Eğer yeni çözüm kabul edilirse, populasyon ve fitness değerlerini güncelliyoruz.
#Aynı zamanda en iyi çözümü de güncelledim.
        
    
        # Yıldız nokta ileta işlemi
        sorted_indices = np.argsort(population_fitness)
        new_population = np.empty_like(population)
        
        for i in range(population_size):
            cuckoo_index = random.randint(0, population_size - 1)
            host_index = sorted_indices[i]
            
            if i == cuckoo_index:
                levy = np.random.standard_cauchy(dimensions) * 0.01
                new_solution = population[host_index] + levy
                new_solution = np.clip(new_solution, lower_bound, upper_bound)
                new_fitness = objective(new_solution)
                if new_fitness < population_fitness[cuckoo_index]:
                    new_population[i] = new_solution
                    population_fitness[cuckoo_index] = new_fitness  # Fitness değerini güncelle
                else:
                    new_population[i] = population[host_index]
            else:
                new_population[i] = population[host_index]
        
        population = new_population
        
#Yıldız nokta ileta" işlemini uyguluyoruz.
#population_fitness listesini sıralayarak, en iyi çözümlerin indekslerini elde ediyoruz.
#Her çözüm için, belirli bir olasılıkla bir "yıldız nokta" oluşturuyoruz. Bu, Cauchy dağılımına göre rasgele bir değer ekleyerek elde edilir.
#Yıldız noktayı mevcut çözümle toplayıp aralığa sığdırıyoruz.
#Yıldız noktanın fitness değerini hesaplayıp, eğer mevcut çözümün fitness değerinden daha iyi ise yeni çözümü kabul ediyoruz.
#Kabul edilmezse, mevcut çözümü koruyoruz.
    
    return best_solution, best_fitness

if __name__ == "__main__":
    # Parametreler
    dimensions = 10
    population_size = 30
    generations = 1000

    # Guguk Kuşu Algoritması'nı çalıştır
    best_solution, best_fitness = cuckoo_search(objective_function, dimensions, population_size, generations)

    print("En iyi çözüm:", best_solution)
    print("En iyi fitness değeri:", best_fitness)
    
#if __name__ == "__main__": ifadesi, bu kod parçasının direkt olarak çalıştırıldığını kontrol eder.
#Bu sayede, bu kod parçası başka bir dosyaya aktarıldığında çalıştırılmaz.
#dimensions, population_size ve generations değişkenleri, Guguk Kuşu Algoritması'nın çalıştırılması için gerekli parametrelerdir. 
#Bu değerler, çözüm boyutunu, populasyon boyutunu ve iterasyon sayısını belirtir.
#cuckoo_search fonksiyonu, belirtilen parametrelerle çağrılarak Guguk Kuşu Algoritması'nı çalıştırır.
#Bu fonksiyonun döndürdüğü en iyi çözüm ve en iyi fitness değeri best_solution ve best_fitness değişkenlerine atanır.
#print ifadeleri, elde edilen sonuçları ekrana basar. En iyi çözümü ve en iyi fitness değerini gösterir.


# In[ ]:




