//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformclipboard.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_CLIPBOARD)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformclipboard.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QPlatformClipboard that Python can take functions over in. Every QPlatformClipboard
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_CLIPBOARD)
typedef void * (*CuteQPlatformClipboardCall0)(const void *, int, int *);
#endif  // !defined(QT_NO_CLIPBOARD)
#if !defined(QT_NO_CLIPBOARD)
typedef void (*CuteQPlatformClipboardCall1)(const void *, QMimeData *, int, int *);
#endif  // !defined(QT_NO_CLIPBOARD)
#if !defined(QT_NO_CLIPBOARD)
typedef bool (*CuteQPlatformClipboardCall2)(const void *, int, int *);
#endif  // !defined(QT_NO_CLIPBOARD)
#if !defined(QT_NO_CLIPBOARD)
typedef bool (*CuteQPlatformClipboardCall3)(const void *, int, int *);
#endif  // !defined(QT_NO_CLIPBOARD)
class CuteQPlatformClipboard : public QPlatformClipboard {
public:
  using QPlatformClipboard::QPlatformClipboard;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_CLIPBOARD)
    if (!std::strcmp(key, "_ZN18QPlatformClipboard8mimeDataEN10QClipboard4ModeE")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_CLIPBOARD)
#if !defined(QT_NO_CLIPBOARD)
    if (!std::strcmp(key, "_ZN18QPlatformClipboard11setMimeDataEP9QMimeDataN10QClipboard4ModeE")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_CLIPBOARD)
#if !defined(QT_NO_CLIPBOARD)
    if (!std::strcmp(key, "_ZNK18QPlatformClipboard12supportsModeEN10QClipboard4ModeE")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_CLIPBOARD)
#if !defined(QT_NO_CLIPBOARD)
    if (!std::strcmp(key, "_ZNK18QPlatformClipboard8ownsModeEN10QClipboard4ModeE")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_CLIPBOARD)
    return false;
  }

#if !defined(QT_NO_CLIPBOARD)
  //  QMimeData *QPlatformClipboard::mimeData(QClipboard::Mode mode)
  QMimeData *mimeData(QClipboard::Mode mode) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformClipboardCall0 call = reinterpret_cast<CuteQPlatformClipboardCall0>(taken[0]);
      void * given = call(this, static_cast<int>(mode), &handled);
      if (handled) return static_cast<QMimeData *>(given);
    }
    return QPlatformClipboard::mimeData(mode);
  }
#endif  // !defined(QT_NO_CLIPBOARD)

#if !defined(QT_NO_CLIPBOARD)
  //  void QPlatformClipboard::setMimeData(QMimeData *data,
  //      QClipboard::Mode mode)
  void setMimeData(QMimeData *data, QClipboard::Mode mode) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformClipboardCall1 call = reinterpret_cast<CuteQPlatformClipboardCall1>(taken[1]);
      call(this, data, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QPlatformClipboard::setMimeData(data, mode);
  }
#endif  // !defined(QT_NO_CLIPBOARD)

#if !defined(QT_NO_CLIPBOARD)
  //  bool QPlatformClipboard::supportsMode(QClipboard::Mode mode) const
  bool supportsMode(QClipboard::Mode mode) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformClipboardCall2 call = reinterpret_cast<CuteQPlatformClipboardCall2>(taken[2]);
      bool given = call(this, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QPlatformClipboard::supportsMode(mode);
  }
#endif  // !defined(QT_NO_CLIPBOARD)

#if !defined(QT_NO_CLIPBOARD)
  //  bool QPlatformClipboard::ownsMode(QClipboard::Mode mode) const
  bool ownsMode(QClipboard::Mode mode) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformClipboardCall3 call = reinterpret_cast<CuteQPlatformClipboardCall3>(taken[3]);
      bool given = call(this, static_cast<int>(mode), &handled);
      if (handled) return given;
    }
    return QPlatformClipboard::ownsMode(mode);
  }
#endif  // !defined(QT_NO_CLIPBOARD)
};

//  QPlatformClipboard::QPlatformClipboard()
extern "C" Q_DECL_EXPORT
QPlatformClipboard *ritual_ZN18QPlatformClipboardC1Ev() {
  return new CuteQPlatformClipboard();
}

//  QPlatformClipboard::~QPlatformClipboard()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformClipboardD1Ev(QPlatformClipboard *self) {
  delete self;
}

//  QMimeData *QPlatformClipboard::mimeData(QClipboard::Mode mode)
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZN18QPlatformClipboard8mimeDataEN10QClipboard4ModeE(
    QPlatformClipboard *self,
    QClipboard::Mode mode) {
  return self->mimeData(mode);
}

//  void QPlatformClipboard::setMimeData(QMimeData *data, QClipboard::Mode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformClipboard11setMimeDataEP9QMimeDataN10QClipboard4ModeE(
    QPlatformClipboard *self,
    QMimeData *data,
    QClipboard::Mode mode) {
  self->setMimeData(data, mode);
}

//  bool QPlatformClipboard::supportsMode(QClipboard::Mode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QPlatformClipboard12supportsModeEN10QClipboard4ModeE(
    const QPlatformClipboard *self,
    QClipboard::Mode mode) {
  return self->supportsMode(mode);
}

//  bool QPlatformClipboard::ownsMode(QClipboard::Mode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QPlatformClipboard8ownsModeEN10QClipboard4ModeE(
    const QPlatformClipboard *self,
    QClipboard::Mode mode) {
  return self->ownsMode(mode);
}

//  void QPlatformClipboard::emitChanged(QClipboard::Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformClipboard11emitChangedEN10QClipboard4ModeE(
    QPlatformClipboard *self,
    QClipboard::Mode mode) {
  self->emitChanged(mode);
}

//  a Python function taken by a CuteQPlatformClipboard, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformClipboard(
    QPlatformClipboard *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformClipboard *>(self)->take(key, call);
}

//  QMimeData *QPlatformClipboard::mimeData(QClipboard::Mode mode)
extern "C" Q_DECL_EXPORT
QMimeData *ritual_own_ZN18QPlatformClipboard8mimeDataEN10QClipboard4ModeE(
    QPlatformClipboard *self,
    QClipboard::Mode mode) {
  return self->QPlatformClipboard::mimeData(mode);
}

//  void QPlatformClipboard::setMimeData(QMimeData *data, QClipboard::Mode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QPlatformClipboard11setMimeDataEP9QMimeDataN10QClipboard4ModeE(
    QPlatformClipboard *self,
    QMimeData *data,
    QClipboard::Mode mode) {
  self->QPlatformClipboard::setMimeData(data, mode);
}

//  bool QPlatformClipboard::supportsMode(QClipboard::Mode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QPlatformClipboard12supportsModeEN10QClipboard4ModeE(
    const QPlatformClipboard *self,
    QClipboard::Mode mode) {
  return self->QPlatformClipboard::supportsMode(mode);
}

//  bool QPlatformClipboard::ownsMode(QClipboard::Mode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QPlatformClipboard8ownsModeEN10QClipboard4ModeE(
    const QPlatformClipboard *self,
    QClipboard::Mode mode) {
  return self->QPlatformClipboard::ownsMode(mode);
}

#endif  // !defined(QT_NO_CLIPBOARD)
