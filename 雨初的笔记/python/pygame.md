+ ```python
  pygame.display.update()
  # 让最近绘制的屏幕可见    
  pygame.display.flip()
  ```

+ ```python
  pygame.display.set_mode((1200, 800)) # 传进去的是一个元组，宽和高 
  ```

+ 设置背景颜色

  ```python
  bg_color = (230, 230, 23)
  # 每次循环时都重绘屏幕
  screen.fill(bg_color)
  # 让最近绘制的屏幕可见       
  pygame.display.flip()
  ```

+ 添加飞船图像

  ```python
  # 载入背景图片  pygame.image.load直接读取图片
  background_img = pygame.image.load('data\\img\\background.png')
  # 得到相关的矩形参数
  background_img_rect = background_img.get_rect()
  background_img = pygame.image.load('data\\img\\background.png')
  # 设置背景图片
  screen.blit(background_img, background_img_rect)	
  ```

## TODOS

+ 要让BOSS出现的时间随机
+ BOSS隔一段时间出现
+ 子弹和子弹碰撞回消失
+ 被击中后设置为被击中的图片



## TODOS

- [x] 普通敌机和BOSS敌机都会**随机左右移动**

- [x] BOSS敌机在**同一时间只会出现一架**

- [x] 普通敌机需要**两发**子弹摧毁，BOSS敌机需要**5发**子弹

- [x] 击落BOSS敌机奖励**100积分**

- [x] BOSS敌机**每隔5秒发射一颗子弹**，玩家发射的子弹和BOSS发射的子弹相撞**可以抵消**，如果**被BOSS敌机发射的子弹击中则游戏结束**

- [x] 拿到炸弹时候显示炸弹个数

- [x] **第一个炸弹**在**100分**的时候出现，之后每获取**1000分**出现一个炸弹

- [x] 每**0.05秒**发射一个子弹

  



## 要求

+ 打印装订前3张
+ ![image-20200917080627699](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200917080627699.png)
+ 