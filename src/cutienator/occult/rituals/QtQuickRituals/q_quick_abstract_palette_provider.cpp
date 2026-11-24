//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickabstractpaletteprovider_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickabstractpaletteprovider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpalette.h>
#include <cstring>

//  A QQuickAbstractPaletteProvider that Python can take functions over in. Every QQuickAbstractPaletteProvider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QPalette * (*CuteQQuickAbstractPaletteProviderCall0)(const void *, int *);
typedef const QPalette * (*CuteQQuickAbstractPaletteProviderCall1)(const void *, const QPalette *, int *);
class CuteQQuickAbstractPaletteProvider : public QQuickAbstractPaletteProvider {
public:
  using QQuickAbstractPaletteProvider::QQuickAbstractPaletteProvider;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK29QQuickAbstractPaletteProvider14defaultPaletteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QQuickAbstractPaletteProvider13parentPaletteERK8QPalette")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QPalette QQuickAbstractPaletteProvider::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAbstractPaletteProviderCall0 call = reinterpret_cast<CuteQQuickAbstractPaletteProviderCall0>(taken[0]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QPalette QQuickAbstractPaletteProvider::parentPalette(const QPalette
  //      &fallbackPalette) const
  QPalette parentPalette(const QPalette &fallbackPalette) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAbstractPaletteProviderCall1 call = reinterpret_cast<CuteQQuickAbstractPaletteProviderCall1>(taken[1]);
      const QPalette * given = call(this, &fallbackPalette, &handled);
      if (handled && given) return *given;
    }
    return QQuickAbstractPaletteProvider::parentPalette(fallbackPalette);
  }
};

//  QQuickAbstractPaletteProvider::~QQuickAbstractPaletteProvider()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickAbstractPaletteProviderD1Ev(
    QQuickAbstractPaletteProvider *self) {
  delete self;
}

//  QPalette QQuickAbstractPaletteProvider::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK29QQuickAbstractPaletteProvider14defaultPaletteEv(
    const QQuickAbstractPaletteProvider *self) {
  return new QPalette(self->defaultPalette());
}

//  QPalette QQuickAbstractPaletteProvider::parentPalette(const QPalette
//      &fallbackPalette) const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK29QQuickAbstractPaletteProvider13parentPaletteERK8QPalette(
    const QQuickAbstractPaletteProvider *self,
    const QPalette *fallbackPalette) {
  return new QPalette(self->parentPalette(*fallbackPalette));
}

//  a Python function taken by a CuteQQuickAbstractPaletteProvider, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAbstractPaletteProvider(
    QQuickAbstractPaletteProvider *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAbstractPaletteProvider *>(self)->take(key, call);
}

//  QPalette QQuickAbstractPaletteProvider::parentPalette(const QPalette
//      &fallbackPalette) const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK29QQuickAbstractPaletteProvider13parentPaletteERK8QPalette(
    const QQuickAbstractPaletteProvider *self,
    const QPalette *fallbackPalette) {
  return new QPalette(
      self->QQuickAbstractPaletteProvider::parentPalette(
          *fallbackPalette));
}
