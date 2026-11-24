//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoaprequest_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoaprequest_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qcoaprequest_p.h"
#include <QtCore/qmath.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/QDebug>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcoap/src/coap/qcoaprequest.cpp, line 287, as _ZN12QCoapRequest6d_funcEv
inline QCoapRequestPrivate* QCoapRequest::d_func()
{
    return static_cast<QCoapRequestPrivate*>(d_ptr.data());
}

//  from ../qtcoap/src/coap/qcoaprequest.cpp, line 30, as _ZN19QCoapRequestPrivateD1Ev
inline QCoapRequestPrivate::~QCoapRequestPrivate()
{
}

//  from ../qtcoap/src/coap/qcoaprequest.cpp, line 34, as _ZNK19QCoapRequestPrivate5cloneEv
inline QCoapRequestPrivate *QCoapRequestPrivate::clone() const
{
    return new QCoapRequestPrivate(*this);
}
//  -----------------------------------------------------------------------

//  A QCoapRequestPrivate that Python can take functions over in. Every QCoapRequestPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQCoapRequestPrivateCall0)(const void *, int *);
class CuteQCoapRequestPrivate : public QCoapRequestPrivate {
public:
  using QCoapRequestPrivate::QCoapRequestPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK19QCoapMessagePrivate5cloneEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QCoapRequestPrivate *QCoapRequestPrivate::clone() const
  QCoapRequestPrivate *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCoapRequestPrivateCall0 call = reinterpret_cast<CuteQCoapRequestPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCoapRequestPrivate *>(given);
    }
    return QCoapRequestPrivate::clone();
  }
};

//  QCoapRequestPrivate::~QCoapRequestPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCoapRequestPrivateD1Ev(QCoapRequestPrivate *self) {
  delete self;
}

//  QCoapRequestPrivate *QCoapRequestPrivate::clone() const
extern "C" Q_DECL_EXPORT
QCoapRequestPrivate *ritual_ZNK19QCoapRequestPrivate5cloneEv(
    const QCoapRequestPrivate *self) {
  return self->clone();
}

//  a Python function taken by a CuteQCoapRequestPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCoapRequestPrivate(
    QCoapRequestPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCoapRequestPrivate *>(self)->take(key, call);
}
