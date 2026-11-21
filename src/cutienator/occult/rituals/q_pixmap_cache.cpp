//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpixmapcache.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpixmapcache.h>
#include <QtCore/qstring.h>
#include <QtGui/qpixmap.h>

//  int QPixmapCache::cacheLimit()
extern "C" Q_DECL_EXPORT
int ritual_ZN12QPixmapCache10cacheLimitEv() {
  return QPixmapCache::cacheLimit();
}

//  void QPixmapCache::setCacheLimit(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPixmapCache13setCacheLimitEi(int a0) {
  QPixmapCache::setCacheLimit(a0);
}

//  bool QPixmapCache::find(const QString &key, QPixmap *pixmap)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QPixmapCache4findERK7QStringP7QPixmap(
    const QString *key,
    QPixmap *pixmap) {
  return QPixmapCache::find(*key, pixmap);
}

//  bool QPixmapCache::find(const Key &key, QPixmap *pixmap)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QPixmapCache4findERKNS_3KeyEP7QPixmap(
    const QPixmapCache::Key *key,
    QPixmap *pixmap) {
  return QPixmapCache::find(*key, pixmap);
}

//  bool QPixmapCache::insert(const QString &key, const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QPixmapCache6insertERK7QStringRK7QPixmap(
    const QString *key,
    const QPixmap *pixmap) {
  return QPixmapCache::insert(*key, *pixmap);
}

//  Key QPixmapCache::insert(const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
QPixmapCache::Key *ritual_ZN12QPixmapCache6insertERK7QPixmap(
    const QPixmap *pixmap) {
  return new QPixmapCache::Key(QPixmapCache::insert(*pixmap));
}

//  bool QPixmapCache::replace(const Key &key, const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QPixmapCache7replaceERKNS_3KeyERK7QPixmap(
    const QPixmapCache::Key *key,
    const QPixmap *pixmap) {
  return QPixmapCache::replace(*key, *pixmap);
}

//  void QPixmapCache::remove(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPixmapCache6removeERK7QString(const QString *key) {
  QPixmapCache::remove(*key);
}

//  void QPixmapCache::remove(const Key &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPixmapCache6removeERKNS_3KeyE(
    const QPixmapCache::Key *key) {
  QPixmapCache::remove(*key);
}

//  void QPixmapCache::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPixmapCache5clearEv() {
  QPixmapCache::clear();
}

//  QPixmapCache::~QPixmapCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPixmapCacheD1Ev(QPixmapCache *self) {
  delete self;
}
