//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qfscompleter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(fscompleter)
#if QT_CONFIG(fscompleter)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qfscompleter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QFSCompleter that Python can take functions over in. Every QFSCompleter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(completer)
#if QT_CONFIG(fscompleter)
typedef QString * (*CuteQFSCompleterCall0)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(fscompleter)
#endif  // QT_CONFIG(completer)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(completer)
typedef bool (*CuteQFSCompleterCall1)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(completer)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(completer)
typedef bool (*CuteQFSCompleterCall2)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(completer)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFSCompleterCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFSCompleterCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFSCompleterCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFSCompleterCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFSCompleterCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQFSCompleter : public QFSCompleter {
public:
  using QFSCompleter::QFSCompleter;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(completer)
#if QT_CONFIG(fscompleter)
    if (!std::strcmp(key, "_ZNK10QCompleter13pathFromIndexERK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(fscompleter)
#endif  // QT_CONFIG(completer)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(completer)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(completer)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(completer)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(completer)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(completer)
#if QT_CONFIG(fscompleter)
  //  QString QFSCompleter::pathFromIndex(const QModelIndex &index) const
  QString pathFromIndex(const QModelIndex &index) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFSCompleterCall0 call = reinterpret_cast<CuteQFSCompleterCall0>(taken[0]);
      QString * given = call(this, &index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QFSCompleter::pathFromIndex(index);
  }
#endif  // QT_CONFIG(fscompleter)
#endif  // QT_CONFIG(completer)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(completer)
  //  bool QCompleter::eventFilter(QObject *o, QEvent *e)
  bool eventFilter(QObject *o, QEvent *e) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFSCompleterCall1 call = reinterpret_cast<CuteQFSCompleterCall1>(taken[1]);
      bool given = call(this, o, e, &handled);
      if (handled) return given;
    }
    return QCompleter::eventFilter(o, e);
  }
#endif  // QT_CONFIG(completer)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(completer)
  //  bool QCompleter::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQFSCompleterCall2 call = reinterpret_cast<CuteQFSCompleterCall2>(taken[2]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QCompleter::event(a0);
  }
#endif  // QT_CONFIG(completer)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFSCompleterCall3 call = reinterpret_cast<CuteQFSCompleterCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQFSCompleterCall4 call = reinterpret_cast<CuteQFSCompleterCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQFSCompleterCall5 call = reinterpret_cast<CuteQFSCompleterCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQFSCompleterCall6 call = reinterpret_cast<CuteQFSCompleterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQFSCompleterCall7 call = reinterpret_cast<CuteQFSCompleterCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QFSCompleter::QFSCompleter(QFileSystemModel *model, QObject *parent)
extern "C" Q_DECL_EXPORT
QFSCompleter *ritual_ZN12QFSCompleterC1EP16QFileSystemModelP7QObject(
    QFileSystemModel *model,
    QObject *parent) {
  return new CuteQFSCompleter(model, parent);
}

//  QString QFSCompleter::pathFromIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QFSCompleter13pathFromIndexERK11QModelIndex(
    const QFSCompleter *self,
    const QModelIndex *index) {
  return new QString(self->pathFromIndex(*index));
}

//  QStringList QFSCompleter::splitPath(const QString &path) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK12QFSCompleter9splitPathERK7QString(
    const QFSCompleter *self,
    const QString *path) {
  return new QList<QString>(self->splitPath(*path));
}

//  a Python function taken by a CuteQFSCompleter, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFSCompleter(
    QFSCompleter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFSCompleter *>(self)->take(key, call);
}

//  QString QFSCompleter::pathFromIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK12QFSCompleter13pathFromIndexERK11QModelIndex(
    const QFSCompleter *self,
    const QModelIndex *index) {
  return new QString(self->QFSCompleter::pathFromIndex(*index));
}

#endif  // QT_CONFIG(fscompleter)
#endif  // QT_CONFIG(fscompleter)
