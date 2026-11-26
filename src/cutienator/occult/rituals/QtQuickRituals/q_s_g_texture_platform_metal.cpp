//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(metal)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSGTexturePlatformMetal that Python can take functions over in. Every QSGTexturePlatformMetal
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(metal) || defined(Q_QDOC)
#if QT_CONFIG(metal)
typedef void * (*CuteQSGTexturePlatformMetalCall0)(const void *, int *);
#endif  // QT_CONFIG(metal)
#endif  // QT_CONFIG(metal) || defined(Q_QDOC)
class CuteQSGTexturePlatformMetal : public QSGTexturePlatformMetal {
public:
  using QSGTexturePlatformMetal::QSGTexturePlatformMetal;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(metal) || defined(Q_QDOC)
#if QT_CONFIG(metal)
    if (!std::strcmp(key, "_ZNK16QNativeInterface15QSGMetalTexture13nativeTextureEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(metal)
#endif  // QT_CONFIG(metal) || defined(Q_QDOC)
    return false;
  }

#if QT_CONFIG(metal) || defined(Q_QDOC)
#if QT_CONFIG(metal)
  //  id QSGTexturePlatformMetal::nativeTexture() const
  id nativeTexture() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGTexturePlatformMetalCall0 call = reinterpret_cast<CuteQSGTexturePlatformMetalCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<id>(given);
    }
    return QSGTexturePlatformMetal::nativeTexture();
  }
#endif  // QT_CONFIG(metal)
#endif  // QT_CONFIG(metal) || defined(Q_QDOC)
};

//  QSGTexturePlatformMetal::QSGTexturePlatformMetal(QSGTexture *t)
extern "C" Q_DECL_EXPORT
QSGTexturePlatformMetal *ritual_ZN23QSGTexturePlatformMetalC1EP10QSGTexture(
    QSGTexture *t) {
  return new CuteQSGTexturePlatformMetal(t);
}

//  id QSGTexturePlatformMetal::nativeTexture() const
extern "C" Q_DECL_EXPORT
id ritual_ZNK23QSGTexturePlatformMetal13nativeTextureEv(
    const QSGTexturePlatformMetal *self) {
  return self->nativeTexture();
}

//  a Python function taken by a CuteQSGTexturePlatformMetal, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGTexturePlatformMetal(
    QSGTexturePlatformMetal *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGTexturePlatformMetal *>(self)->take(key, call);
}

//  id QSGTexturePlatformMetal::nativeTexture() const
extern "C" Q_DECL_EXPORT
id ritual_own_ZNK23QSGTexturePlatformMetal13nativeTextureEv(
    const QSGTexturePlatformMetal *self) {
  return self->QSGTexturePlatformMetal::nativeTexture();
}

#endif  // QT_CONFIG(metal)
