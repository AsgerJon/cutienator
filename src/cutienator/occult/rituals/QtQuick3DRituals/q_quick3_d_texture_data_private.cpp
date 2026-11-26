//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dtexturedata_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dtexturedata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/qquick3dtexturedata.h>
#include <QtQuick3D/private/qquick3dtexturedata_p.h>
#include <QtQuick3DUtils/private/qssgutils_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendertexturedata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/quick3d/qquick3dtexturedata.cpp, line 218, as _ZN26QQuick3DTextureDataPrivateC1Ev
inline QQuick3DTextureDataPrivate::QQuick3DTextureDataPrivate()
    : QQuick3DObjectPrivate(QQuick3DTextureDataPrivate::Type::TextureData)
{

}
//  -----------------------------------------------------------------------

//  A QQuick3DTextureDataPrivate that Python can take functions over in. Every QQuick3DTextureDataPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DTextureDataPrivateCall0)(const void *, int *);
class CuteQQuick3DTextureDataPrivate : public QQuick3DTextureDataPrivate {
public:
  using QQuick3DTextureDataPrivate::QQuick3DTextureDataPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QQuick3DObjectPrivate12updatePolishEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QQuick3DObjectPrivate::updatePolish()
  void updatePolish() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DTextureDataPrivateCall0 call = reinterpret_cast<CuteQQuick3DTextureDataPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObjectPrivate::updatePolish();
  }
};

//  QQuick3DTextureDataPrivate::QQuick3DTextureDataPrivate()
extern "C" Q_DECL_EXPORT
QQuick3DTextureDataPrivate *ritual_ZN26QQuick3DTextureDataPrivateC1Ev() {
  return new CuteQQuick3DTextureDataPrivate();
}

//  a Python function taken by a CuteQQuick3DTextureDataPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DTextureDataPrivate(
    QQuick3DTextureDataPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DTextureDataPrivate *>(self)->take(key, call);
}
