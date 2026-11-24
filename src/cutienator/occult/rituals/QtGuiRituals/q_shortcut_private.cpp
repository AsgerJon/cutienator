//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qshortcut_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qshortcut.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qshortcut_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QShortcutPrivate that Python can take functions over in. Every QShortcutPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQShortcutPrivateCall0)(const void *, int *);
class CuteQShortcutPrivate : public QShortcutPrivate {
public:
  using QShortcutPrivate::QShortcutPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QShortcutPrivate15handleWhatsThisEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  bool QShortcutPrivate::handleWhatsThis()
  bool handleWhatsThis() override {
    if (taken[0]) {
      int handled = 0;
      CuteQShortcutPrivateCall0 call = reinterpret_cast<CuteQShortcutPrivateCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QShortcutPrivate::handleWhatsThis();
  }
};

//  QShortcut *QShortcutPrivate::q_func()
extern "C" Q_DECL_EXPORT
QShortcut *ritual_ZN16QShortcutPrivate6q_funcEv(QShortcutPrivate *self) {
  return self->q_func();
}

//  const QShortcut *QShortcutPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QShortcut *ritual_ZNK16QShortcutPrivate6q_funcEv(
    const QShortcutPrivate *self) {
  return self->q_func();
}

//  QShortcutPrivate::QShortcutPrivate()
extern "C" Q_DECL_EXPORT
QShortcutPrivate *ritual_ZN16QShortcutPrivateC1Ev() {
  return new CuteQShortcutPrivate();
}

//  bool QShortcutPrivate::handleWhatsThis()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QShortcutPrivate15handleWhatsThisEv(QShortcutPrivate *self) {
  return self->handleWhatsThis();
}

//  bool QShortcutPrivate::simpleContextMatcher(QObject *object,
//      Qt::ShortcutContext context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QShortcutPrivate20simpleContextMatcherEP7QObjectN2Qt15ShortcutContextE(
    QObject *object,
    Qt::ShortcutContext context) {
  return QShortcutPrivate::simpleContextMatcher(object, context);
}

//  a Python function taken by a CuteQShortcutPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QShortcutPrivate(
    QShortcutPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQShortcutPrivate *>(self)->take(key, call);
}

//  bool QShortcutPrivate::handleWhatsThis()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QShortcutPrivate15handleWhatsThisEv(
    QShortcutPrivate *self) {
  return self->QShortcutPrivate::handleWhatsThis();
}
