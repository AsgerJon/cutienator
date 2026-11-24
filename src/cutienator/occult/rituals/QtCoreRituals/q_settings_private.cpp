//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsettings_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(settings)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qsettings.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsettings.h>
#include <QtCore/private/qsettings_p.h>
#include <QtCore/qcache.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qdir.h>
#include <QtCore/qfile.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qlibraryinfo.h>
#include <QtCore/private/qlocking_p.h>
#include <QtCore/qmutex.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qstandardpaths.h>
#include <QtCore/private/qstringconverter_p.h>
#include <QtCore/qtemporaryfile.h>
#include <QtCore/private/qtools_p.h>
#ifndef QT_BOOTSTRAPPED
#include <QtCore/qsavefile.h>
#include <QtCore/qlockfile.h>
#endif
#ifdef Q_OS_VXWORKS
#  include <ioLib.h>
#endif
#include <algorithm>
#include <stdlib.h>
#ifdef Q_OS_WIN
#  include <QtCore/qt_windows.h>
#  include <shlobj.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qsettings.cpp, line 299, as _ZN16QSettingsPrivate17beginGroupOrArrayERK14QSettingsGroup
inline void QSettingsPrivate::beginGroupOrArray(const QSettingsGroup &group)
{
    groupStack.push(group);
    const QString name = group.name();
    if (!name.isEmpty())
        groupPrefix += name + u'/';
}

//  from src/corelib/io/qsettings.cpp, line 312, as _ZNK16QSettingsPrivate9setStatusEN9QSettings6StatusE
inline void QSettingsPrivate::setStatus(QSettings::Status status) const
{
    if (status == QSettings::NoError || this->status == QSettings::NoError)
        this->status = status;
}

//  from src/corelib/io/qsettings.cpp, line 324, as _ZN16QSettingsPrivate13requestUpdateEv
inline void QSettingsPrivate::requestUpdate()
{
    if (!pendingChanges) {
        pendingChanges = true;
#ifndef QT_NO_QOBJECT
        Q_Q(QSettings);
        QCoreApplication::postEvent(q, new QEvent(QEvent::UpdateRequest));
#else
        update();
#endif
    }
}

//  from src/corelib/io/qsettings.cpp, line 318, as _ZN16QSettingsPrivate6updateEv
inline void QSettingsPrivate::update()
{
    flush();
    pendingChanges = false;
}

//  from src/corelib/io/qsettings.cpp, line 841, as _ZN16QSettingsPrivate9splitArgsERK7QStringx
inline QStringList QSettingsPrivate::splitArgs(const QString &s, qsizetype idx)
{
    qsizetype l = s.size();
    Q_ASSERT(l > 0);
    Q_ASSERT(s.at(idx) == u'(');
    Q_ASSERT(s.at(l - 1) == u')');

    QStringList result;
    QString item;

    for (++idx; idx < l; ++idx) {
        QChar c = s.at(idx);
        if (c == u')') {
            Q_ASSERT(idx == l - 1);
            result.append(item);
        } else if (c == u' ') {
            result.append(item);
            item.clear();
        } else {
            item.append(c);
        }
    }

    return result;
}
//  -----------------------------------------------------------------------

//  A QSettingsPrivate that Python can take functions over in. Every QSettingsPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSettingsPrivateCall0)(const void *, const QString *, int *);
typedef void (*CuteQSettingsPrivateCall1)(const void *, const QString *, const QVariant *, int *);
typedef void (*CuteQSettingsPrivateCall2)(const void *, int *);
typedef void (*CuteQSettingsPrivateCall3)(const void *, int *);
typedef void (*CuteQSettingsPrivateCall4)(const void *, int *);
typedef bool (*CuteQSettingsPrivateCall5)(const void *, int *);
typedef QString * (*CuteQSettingsPrivateCall6)(const void *, int *);
class CuteQSettingsPrivate : public QSettingsPrivate {
public:
  using QSettingsPrivate::QSettingsPrivate;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QSettingsPrivate6removeERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSettingsPrivate3setERK7QStringRK8QVariant")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSettingsPrivate5clearEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSettingsPrivate4syncEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSettingsPrivate5flushEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QSettingsPrivate10isWritableEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QSettingsPrivate8fileNameEv")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  void QSettingsPrivate::remove(const QString &key)
  void remove(const QString &key) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSettingsPrivateCall0 call = reinterpret_cast<CuteQSettingsPrivateCall0>(taken[0]);
      call(this, &key, &handled);
      if (handled) return;
    }
  }

  //  void QSettingsPrivate::set(const QString &key, const QVariant &value)
  void set(const QString &key, const QVariant &value) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSettingsPrivateCall1 call = reinterpret_cast<CuteQSettingsPrivateCall1>(taken[1]);
      call(this, &key, &value, &handled);
      if (handled) return;
    }
  }

  //  void QSettingsPrivate::clear()
  void clear() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSettingsPrivateCall2 call = reinterpret_cast<CuteQSettingsPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSettingsPrivate::sync()
  void sync() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSettingsPrivateCall3 call = reinterpret_cast<CuteQSettingsPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSettingsPrivate::flush()
  void flush() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSettingsPrivateCall4 call = reinterpret_cast<CuteQSettingsPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  bool QSettingsPrivate::isWritable() const
  bool isWritable() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSettingsPrivateCall5 call = reinterpret_cast<CuteQSettingsPrivateCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QSettingsPrivate::fileName() const
  QString fileName() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSettingsPrivateCall6 call = reinterpret_cast<CuteQSettingsPrivateCall6>(taken[6]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
};

//  QSettings *QSettingsPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSettings *ritual_ZN16QSettingsPrivate6q_funcEv(QSettingsPrivate *self) {
  return self->q_func();
}

//  const QSettings *QSettingsPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSettings *ritual_ZNK16QSettingsPrivate6q_funcEv(
    const QSettingsPrivate *self) {
  return self->q_func();
}

//  QSettingsPrivate::~QSettingsPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSettingsPrivateD1Ev(QSettingsPrivate *self) {
  delete self;
}

//  void QSettingsPrivate::remove(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSettingsPrivate6removeERK7QString(
    QSettingsPrivate *self,
    const QString *key) {
  self->remove(*key);
}

//  void QSettingsPrivate::set(const QString &key, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSettingsPrivate3setERK7QStringRK8QVariant(
    QSettingsPrivate *self,
    const QString *key,
    const QVariant *value) {
  self->set(*key, *value);
}

//  QStringList QSettingsPrivate::children(const QString &prefix, ChildSpec
//      spec) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK16QSettingsPrivate8childrenERK7QStringNS_9ChildSpecE(
    const QSettingsPrivate *self,
    const QString *prefix,
    QSettingsPrivate::ChildSpec spec) {
  return new QList<QString>(self->children(*prefix, spec));
}

//  void QSettingsPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSettingsPrivate5clearEv(QSettingsPrivate *self) {
  self->clear();
}

//  void QSettingsPrivate::sync()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSettingsPrivate4syncEv(QSettingsPrivate *self) {
  self->sync();
}

//  void QSettingsPrivate::flush()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSettingsPrivate5flushEv(QSettingsPrivate *self) {
  self->flush();
}

//  bool QSettingsPrivate::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSettingsPrivate10isWritableEv(
    const QSettingsPrivate *self) {
  return self->isWritable();
}

//  QString QSettingsPrivate::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QSettingsPrivate8fileNameEv(
    const QSettingsPrivate *self) {
  return new QString(self->fileName());
}

//  void QSettingsPrivate::beginGroupOrArray(const QSettingsGroup &group)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSettingsPrivate17beginGroupOrArrayERK14QSettingsGroup(
    QSettingsPrivate *self,
    const QSettingsGroup *group) {
  self->beginGroupOrArray(*group);
}

//  void QSettingsPrivate::setStatus(QSettings::Status status) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QSettingsPrivate9setStatusEN9QSettings6StatusE(
    const QSettingsPrivate *self,
    QSettings::Status status) {
  self->setStatus(status);
}

//  void QSettingsPrivate::requestUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSettingsPrivate13requestUpdateEv(QSettingsPrivate *self) {
  self->requestUpdate();
}

//  void QSettingsPrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSettingsPrivate6updateEv(QSettingsPrivate *self) {
  self->update();
}

//  QStringList QSettingsPrivate::splitArgs(const QString &s, qsizetype idx)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN16QSettingsPrivate9splitArgsERK7QStringx(
    const QString *s,
    qsizetype idx) {
  return new QList<QString>(QSettingsPrivate::splitArgs(*s, idx));
}

//  a Python function taken by a CuteQSettingsPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSettingsPrivate(
    QSettingsPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSettingsPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(settings)
