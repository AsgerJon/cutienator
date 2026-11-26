//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkaccesscache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkaccesscache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qnetworkaccesscache_p.h>
#include "QtCore/qpointer.h"
#include "QtCore/qdeadlinetimer.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qnetworkaccesscache.cpp, line 37, as _ZN19QNetworkAccessCache15CacheableObjectD2Ev
inline QNetworkAccessCache::CacheableObject::~CacheableObject()
{
#if 0 //def QT_DEBUG
    if (!key.isEmpty() && Ptr()->hasEntry(key))
        qWarning() << "QNetworkAccessCache: object" << (void*)this << "key" << key
                   << "destroyed without being removed from cache first!";
#endif
}

//  from src/network/access/qnetworkaccesscache.cpp, line 30, as _ZN19QNetworkAccessCache15CacheableObjectC1E6QFlagsINS0_6OptionEE
inline QNetworkAccessCache::CacheableObject::CacheableObject(Options options)
    : expires(options & Option::Expires),
      shareable(options & Option::Shareable)
{

}
//  -----------------------------------------------------------------------

//  A QNetworkAccessCache::CacheableObject that Python can take functions over in. Every QNetworkAccessCache::CacheableObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNetworkAccessCache_CacheableObjectCall0)(const void *, int *);
class CuteQNetworkAccessCache_CacheableObject : public QNetworkAccessCache::CacheableObject {
public:
  using QNetworkAccessCache::CacheableObject::CacheableObject;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QNetworkAccessCache15CacheableObject7disposeEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QNetworkAccessCache::CacheableObject::dispose()
  void dispose() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkAccessCache_CacheableObjectCall0 call = reinterpret_cast<CuteQNetworkAccessCache_CacheableObjectCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QNetworkAccessCache::CacheableObject::~CacheableObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QNetworkAccessCache15CacheableObjectD1Ev(
    QNetworkAccessCache::CacheableObject *self) {
  delete self;
}

//  void QNetworkAccessCache::CacheableObject::dispose()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QNetworkAccessCache15CacheableObject7disposeEv(
    QNetworkAccessCache::CacheableObject *self) {
  self->dispose();
}

//  QByteArray QNetworkAccessCache::CacheableObject::cacheKey() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK19QNetworkAccessCache15CacheableObject8cacheKeyEv(
    const QNetworkAccessCache::CacheableObject *self) {
  return new QByteArray(self->cacheKey());
}

//  QNetworkAccessCache::CacheableObject::CacheableObject(Options options)
extern "C" Q_DECL_EXPORT
QNetworkAccessCache::CacheableObject *ritual_ZN19QNetworkAccessCache15CacheableObjectC1E6QFlagsINS0_6OptionEE(
    int options) {
  return new CuteQNetworkAccessCache_CacheableObject(
      QFlags<QNetworkAccessCache::CacheableObject::Option>::fromInt(options));
}

//  a Python function taken by a CuteQNetworkAccessCache_CacheableObject, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkAccessCache_CacheableObject(
    QNetworkAccessCache::CacheableObject *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkAccessCache_CacheableObject *>(self)->take(key, call);
}
