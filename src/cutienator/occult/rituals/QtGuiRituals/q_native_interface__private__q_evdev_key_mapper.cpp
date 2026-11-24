//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qkeymapper_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(evdev) || defined(Q_QDOC)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qkeymapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A QNativeInterface::Private::QEvdevKeyMapper that Python can take functions over in. Every QNativeInterface::Private::QEvdevKeyMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(evdev) || defined(Q_QDOC)
typedef void (*CuteQNativeInterface_Private_QEvdevKeyMapperCall0)(const void *, const QString *, int *);
#endif  // QT_CONFIG(evdev) || defined(Q_QDOC)
#if QT_CONFIG(evdev) || defined(Q_QDOC)
typedef void (*CuteQNativeInterface_Private_QEvdevKeyMapperCall1)(const void *, int *);
#endif  // QT_CONFIG(evdev) || defined(Q_QDOC)
class CuteQNativeInterface_Private_QEvdevKeyMapper : public QNativeInterface::Private::QEvdevKeyMapper {
public:
  using QNativeInterface::Private::QEvdevKeyMapper::QEvdevKeyMapper;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(evdev) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN16QNativeInterface7Private15QEvdevKeyMapper10loadKeymapERK7QString")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(evdev) || defined(Q_QDOC)
#if QT_CONFIG(evdev) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN16QNativeInterface7Private15QEvdevKeyMapper10switchLangEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(evdev) || defined(Q_QDOC)
    return false;
  }

#if QT_CONFIG(evdev) || defined(Q_QDOC)
  //  void QNativeInterface::Private::QEvdevKeyMapper::loadKeymap(const
  //      QString &filename)
  void loadKeymap(const QString &filename) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeInterface_Private_QEvdevKeyMapperCall0 call = reinterpret_cast<CuteQNativeInterface_Private_QEvdevKeyMapperCall0>(taken[0]);
      call(this, &filename, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(evdev) || defined(Q_QDOC)

#if QT_CONFIG(evdev) || defined(Q_QDOC)
  //  void QNativeInterface::Private::QEvdevKeyMapper::switchLang()
  void switchLang() override {
    if (taken[1]) {
      int handled = 0;
      CuteQNativeInterface_Private_QEvdevKeyMapperCall1 call = reinterpret_cast<CuteQNativeInterface_Private_QEvdevKeyMapperCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(evdev) || defined(Q_QDOC)
};

//  QNativeInterface::Private::QEvdevKeyMapper::~QEvdevKeyMapper()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private15QEvdevKeyMapperD1Ev(
    QNativeInterface::Private::QEvdevKeyMapper *self) {
  delete self;
}

//  void QNativeInterface::Private::QEvdevKeyMapper::loadKeymap(const QString
//      &filename)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private15QEvdevKeyMapper10loadKeymapERK7QString(
    QNativeInterface::Private::QEvdevKeyMapper *self,
    const QString *filename) {
  self->loadKeymap(*filename);
}

//  void QNativeInterface::Private::QEvdevKeyMapper::switchLang()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface7Private15QEvdevKeyMapper10switchLangEv(
    QNativeInterface::Private::QEvdevKeyMapper *self) {
  self->switchLang();
}

//  a Python function taken by a
//      CuteQNativeInterface_Private_QEvdevKeyMapper, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNativeInterface_Private_QEvdevKeyMapper(
    QNativeInterface::Private::QEvdevKeyMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNativeInterface_Private_QEvdevKeyMapper *>(self)->take(key, call);
}

#endif  // QT_CONFIG(evdev) || defined(Q_QDOC)
