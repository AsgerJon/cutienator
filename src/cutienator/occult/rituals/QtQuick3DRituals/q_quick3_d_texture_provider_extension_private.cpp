//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dtextureproviderextension_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dtextureproviderextension_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/qquick3dtextureproviderextension.h>
#include <QtQuick3D/private/qquick3dobject_p.h>
#include <QtQuick3D/private/qquick3dtextureproviderextension_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/quick3d/extensions/qquick3dtextureproviderextension.cpp, line 105, as _ZN39QQuick3DTextureProviderExtensionPrivateC1Ev
inline QQuick3DTextureProviderExtensionPrivate::QQuick3DTextureProviderExtensionPrivate()
    : QQuick3DObjectPrivate(QQuick3DObjectPrivate::Type::TextureProvider)
{

}
//  -----------------------------------------------------------------------

//  A QQuick3DTextureProviderExtensionPrivate that Python can take functions over in. Every QQuick3DTextureProviderExtensionPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DTextureProviderExtensionPrivateCall0)(const void *, int *);
class CuteQQuick3DTextureProviderExtensionPrivate : public QQuick3DTextureProviderExtensionPrivate {
public:
  using QQuick3DTextureProviderExtensionPrivate::QQuick3DTextureProviderExtensionPrivate;
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
      CuteQQuick3DTextureProviderExtensionPrivateCall0 call = reinterpret_cast<CuteQQuick3DTextureProviderExtensionPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObjectPrivate::updatePolish();
  }
};

//  QQuick3DTextureProviderExtensionPrivate::QQuick3DTextureProviderExtension
//      Private()
extern "C" Q_DECL_EXPORT
QQuick3DTextureProviderExtensionPrivate *ritual_ZN39QQuick3DTextureProviderExtensionPrivateC1Ev() {
  return new CuteQQuick3DTextureProviderExtensionPrivate();
}

//  a Python function taken by a CuteQQuick3DTextureProviderExtensionPrivate,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DTextureProviderExtensionPrivate(
    QQuick3DTextureProviderExtensionPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DTextureProviderExtensionPrivate *>(self)->take(key, call);
}
