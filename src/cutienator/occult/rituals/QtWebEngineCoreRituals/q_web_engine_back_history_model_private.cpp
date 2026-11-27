//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginehistory_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qtwebenginecoreglobal_p.h>
#include <QtWebEngineCore/QtWebEngineCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginehistory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineCore/qwebenginehistory.h>
#include <QtWebEngineCore/private/qwebenginehistory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebengine/src/core/api/qwebenginehistory.cpp, line 114, as _ZN29QWebEngineHistoryModelPrivateC2EPK24QWebEngineHistoryPrivate
inline QWebEngineHistoryModelPrivate::QWebEngineHistoryModelPrivate(const QWebEngineHistoryPrivate *history)
    : history(history)
{
    Q_ASSERT(history);
}

//  from ../qtwebengine/src/core/api/qwebenginehistory.cpp, line 120, as _ZN29QWebEngineHistoryModelPrivateD2Ev
inline QWebEngineHistoryModelPrivate::~QWebEngineHistoryModelPrivate()
{
}

//  from ../qtwebengine/src/core/api/qwebenginehistory.cpp, line 156, as _ZNK33QWebEngineBackHistoryModelPrivate14offsetForIndexEi
inline int QWebEngineBackHistoryModelPrivate::offsetForIndex(int index) const
{
    return - index - 1;
}

//  from ../qtwebengine/src/core/api/qwebenginehistory.cpp, line 150, as _ZNK33QWebEngineBackHistoryModelPrivate5indexEi
inline int QWebEngineBackHistoryModelPrivate::index(int i) const
{
    Q_ASSERT(i >= 0 && i < count());
    return count() - 1 - i;
}

//  from ../qtwebengine/src/core/api/qwebenginehistory.cpp, line 135, as _ZNK29QWebEngineHistoryModelPrivate5indexEi
inline int QWebEngineHistoryModelPrivate::index(int index) const
{
    return index;
}
//  -----------------------------------------------------------------------

//  A QWebEngineBackHistoryModelPrivate that Python can take functions over in. Every QWebEngineBackHistoryModelPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQWebEngineBackHistoryModelPrivateCall0)(const void *, int *);
typedef int (*CuteQWebEngineBackHistoryModelPrivateCall1)(const void *, int, int *);
typedef int (*CuteQWebEngineBackHistoryModelPrivateCall2)(const void *, int, int *);
class CuteQWebEngineBackHistoryModelPrivate : public QWebEngineBackHistoryModelPrivate {
public:
  using QWebEngineBackHistoryModelPrivate::QWebEngineBackHistoryModelPrivate;
  CuteQWebEngineBackHistoryModelPrivate(const QWebEngineBackHistoryModelPrivate & other) : QWebEngineBackHistoryModelPrivate(other) {}
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK29QWebEngineHistoryModelPrivate5countEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QWebEngineHistoryModelPrivate5indexEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QWebEngineHistoryModelPrivate14offsetForIndexEi")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  int QWebEngineBackHistoryModelPrivate::count() const
  int count() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWebEngineBackHistoryModelPrivateCall0 call = reinterpret_cast<CuteQWebEngineBackHistoryModelPrivateCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWebEngineBackHistoryModelPrivate::count();
  }

  //  int QWebEngineBackHistoryModelPrivate::index(int a0) const
  int index(int a0) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWebEngineBackHistoryModelPrivateCall1 call = reinterpret_cast<CuteQWebEngineBackHistoryModelPrivateCall1>(taken[1]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWebEngineBackHistoryModelPrivate::index(a0);
  }

  //  int QWebEngineBackHistoryModelPrivate::offsetForIndex(int a0) const
  int offsetForIndex(int a0) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQWebEngineBackHistoryModelPrivateCall2 call = reinterpret_cast<CuteQWebEngineBackHistoryModelPrivateCall2>(taken[2]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWebEngineBackHistoryModelPrivate::offsetForIndex(a0);
  }
};

//  int QWebEngineBackHistoryModelPrivate::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK33QWebEngineBackHistoryModelPrivate5countEv(
    const QWebEngineBackHistoryModelPrivate *self) {
  return self->count();
}

//  int QWebEngineBackHistoryModelPrivate::index(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK33QWebEngineBackHistoryModelPrivate5indexEi(
    const QWebEngineBackHistoryModelPrivate *self,
    int a0) {
  return self->index(a0);
}

//  int QWebEngineBackHistoryModelPrivate::offsetForIndex(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK33QWebEngineBackHistoryModelPrivate14offsetForIndexEi(
    const QWebEngineBackHistoryModelPrivate *self,
    int a0) {
  return self->offsetForIndex(a0);
}

//  QWebEngineBackHistoryModelPrivate::~QWebEngineBackHistoryModelPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QWebEngineBackHistoryModelPrivateD1Ev(
    QWebEngineBackHistoryModelPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQWebEngineBackHistoryModelPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebEngineBackHistoryModelPrivate(
    QWebEngineBackHistoryModelPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebEngineBackHistoryModelPrivate *>(self)->take(key, call);
}

//  int QWebEngineBackHistoryModelPrivate::index(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK33QWebEngineBackHistoryModelPrivate5indexEi(
    const QWebEngineBackHistoryModelPrivate *self,
    int a0) {
  return self->QWebEngineBackHistoryModelPrivate::index(a0);
}

//  int QWebEngineBackHistoryModelPrivate::offsetForIndex(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK33QWebEngineBackHistoryModelPrivate14offsetForIndexEi(
    const QWebEngineBackHistoryModelPrivate *self,
    int a0) {
  return self->QWebEngineBackHistoryModelPrivate::offsetForIndex(a0);
}
