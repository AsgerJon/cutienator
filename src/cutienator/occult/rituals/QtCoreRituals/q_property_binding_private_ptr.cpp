//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpropertyprivate.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qpropertyprivate.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qproperty.h>
#include <QtCore/private/qproperty_p.h>
#include <QtCore/qscopedvaluerollback.h>
#include <QtCore/QScopeGuard>
#include <QtCore/qalloc.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/private/qthread_p.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmutex.h>
#include <QtCore/private/qobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/kernel/qproperty.cpp, line 29, as _ZN26QPropertyBindingPrivatePtr5resetEPN9QtPrivate10RefCountedE
inline void QPropertyBindingPrivatePtr::reset(QtPrivate::RefCounted *ptr) noexcept
{
    if (ptr != d) {
        if (ptr)
            ptr->addRef();
        auto *old = std::exchange(d, ptr);
        if (old && !old->deref())
            QPropertyBindingPrivate::destroyAndFreeMemory(static_cast<QPropertyBindingPrivate *>(d));
    }
}
//  -----------------------------------------------------------------------

//  T &QPropertyBindingPrivatePtr::operator*() const
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivatePtr::T *ritual_ZNK26QPropertyBindingPrivatePtrdeEv(
    const QPropertyBindingPrivatePtr *self) {
  return &(self->operator*());
}

//  T *QPropertyBindingPrivatePtr::operator->()
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivatePtr::T *ritual_ZN26QPropertyBindingPrivatePtrptEv(
    QPropertyBindingPrivatePtr *self) {
  return self->operator->();
}

//  T *QPropertyBindingPrivatePtr::operator->() const
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivatePtr::T *ritual_ZNK26QPropertyBindingPrivatePtrptEv(
    const QPropertyBindingPrivatePtr *self) {
  return self->operator->();
}

//  T *QPropertyBindingPrivatePtr::operator QtPrivate::RefCounted *()
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivatePtr::T *ritual_ZN26QPropertyBindingPrivatePtrcvPN9QtPrivate10RefCountedEEv(
    QPropertyBindingPrivatePtr *self) {
  return self->operator QPropertyBindingPrivatePtr::T *();
}

//  const T *QPropertyBindingPrivatePtr::operator const QtPrivate::RefCounted
//      *() const
extern "C" Q_DECL_EXPORT
const QPropertyBindingPrivatePtr::T *ritual_ZNK26QPropertyBindingPrivatePtrcvPKN9QtPrivate10RefCountedEEv(
    const QPropertyBindingPrivatePtr *self) {
  return self->operator const QPropertyBindingPrivatePtr::T *();
}

//  T *QPropertyBindingPrivatePtr::data() const
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivatePtr::T *ritual_ZNK26QPropertyBindingPrivatePtr4dataEv(
    const QPropertyBindingPrivatePtr *self) {
  return self->data();
}

//  T *QPropertyBindingPrivatePtr::get() const
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivatePtr::T *ritual_ZNK26QPropertyBindingPrivatePtr3getEv(
    const QPropertyBindingPrivatePtr *self) {
  return self->get();
}

//  const T *QPropertyBindingPrivatePtr::constData() const
extern "C" Q_DECL_EXPORT
const QPropertyBindingPrivatePtr::T *ritual_ZNK26QPropertyBindingPrivatePtr9constDataEv(
    const QPropertyBindingPrivatePtr *self) {
  return self->constData();
}

//  T *QPropertyBindingPrivatePtr::take()
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivatePtr::T *ritual_ZN26QPropertyBindingPrivatePtr4takeEv(
    QPropertyBindingPrivatePtr *self) {
  return self->take();
}

//  QPropertyBindingPrivatePtr::QPropertyBindingPrivatePtr()
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivatePtr *ritual_ZN26QPropertyBindingPrivatePtrC1Ev() {
  return new QPropertyBindingPrivatePtr();
}

//  QPropertyBindingPrivatePtr::~QPropertyBindingPrivatePtr()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPropertyBindingPrivatePtrD1Ev(
    QPropertyBindingPrivatePtr *self) {
  delete self;
}

//  void QPropertyBindingPrivatePtr::destroyAndFreeMemory()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPropertyBindingPrivatePtr20destroyAndFreeMemoryEv(
    QPropertyBindingPrivatePtr *self) {
  self->destroyAndFreeMemory();
}

//  QPropertyBindingPrivatePtr::QPropertyBindingPrivatePtr(T *data)
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivatePtr *ritual_ZN26QPropertyBindingPrivatePtrC1EPN9QtPrivate10RefCountedE(
    QPropertyBindingPrivatePtr::T *data) {
  return new QPropertyBindingPrivatePtr(data);
}

//  QPropertyBindingPrivatePtr::QPropertyBindingPrivatePtr(const
//      QPropertyBindingPrivatePtr &o)
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivatePtr *ritual_ZN26QPropertyBindingPrivatePtrC1ERKS_(
    const QPropertyBindingPrivatePtr *o) {
  return new QPropertyBindingPrivatePtr(*o);
}

//  void QPropertyBindingPrivatePtr::reset(T *ptr)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPropertyBindingPrivatePtr5resetEPN9QtPrivate10RefCountedE(
    QPropertyBindingPrivatePtr *self,
    QPropertyBindingPrivatePtr::T *ptr) {
  self->reset(ptr);
}

//  QPropertyBindingPrivatePtr &QPropertyBindingPrivatePtr::operator=(const
//      QPropertyBindingPrivatePtr &o)
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivatePtr *ritual_ZN26QPropertyBindingPrivatePtraSERKS_(
    QPropertyBindingPrivatePtr *self,
    const QPropertyBindingPrivatePtr *o) {
  return &(self->operator=(*o));
}

//  QPropertyBindingPrivatePtr &QPropertyBindingPrivatePtr::operator=(T *o)
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivatePtr *ritual_ZN26QPropertyBindingPrivatePtraSEPN9QtPrivate10RefCountedE(
    QPropertyBindingPrivatePtr *self,
    QPropertyBindingPrivatePtr::T *o) {
  return &(self->operator=(o));
}

//  QPropertyBindingPrivatePtr::QPropertyBindingPrivatePtr(QPropertyBindingPr
//      ivatePtr &&o)
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivatePtr *ritual_ZN26QPropertyBindingPrivatePtrC1EOS_(
    QPropertyBindingPrivatePtr *o) {
  return new QPropertyBindingPrivatePtr(std::move(*o));
}

//  QPropertyBindingPrivatePtr
//      &QPropertyBindingPrivatePtr::operator=(QPropertyBindingPrivatePtr
//      &&other)
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivatePtr *ritual_ZN26QPropertyBindingPrivatePtraSEOS_(
    QPropertyBindingPrivatePtr *self,
    QPropertyBindingPrivatePtr *other) {
  return &(self->operator=(std::move(*other)));
}

//  bool QPropertyBindingPrivatePtr::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QPropertyBindingPrivatePtrcvbEv(
    const QPropertyBindingPrivatePtr *self) {
  return self->operator bool();
}

//  bool QPropertyBindingPrivatePtr::operator!() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QPropertyBindingPrivatePtrntEv(
    const QPropertyBindingPrivatePtr *self) {
  return self->operator!();
}

//  void QPropertyBindingPrivatePtr::swap(QPropertyBindingPrivatePtr &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPropertyBindingPrivatePtr4swapERS_(
    QPropertyBindingPrivatePtr *self,
    QPropertyBindingPrivatePtr *other) {
  self->swap(*other);
}

//  bool operator==(const QPropertyBindingPrivatePtr &lhs, const
//      QPropertyBindingPrivatePtr &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK26QPropertyBindingPrivatePtrS1_(
    const QPropertyBindingPrivatePtr *lhs,
    const QPropertyBindingPrivatePtr *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPropertyBindingPrivatePtr &lhs, const
//      QPropertyBindingPrivatePtr &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK26QPropertyBindingPrivatePtrS1_(
    const QPropertyBindingPrivatePtr *lhs,
    const QPropertyBindingPrivatePtr *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QPropertyBindingPrivatePtr &lhs, T *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK26QPropertyBindingPrivatePtrRKPN9QtPrivate10RefCountedE(
    const QPropertyBindingPrivatePtr *lhs,
    QPropertyBindingPrivatePtr::T *const *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPropertyBindingPrivatePtr &lhs, T *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK26QPropertyBindingPrivatePtrRKPN9QtPrivate10RefCountedE(
    const QPropertyBindingPrivatePtr *lhs,
    QPropertyBindingPrivatePtr::T *const *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(T *const &lhs, const QPropertyBindingPrivatePtr &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKPN9QtPrivate10RefCountedERK26QPropertyBindingPrivatePtr(
    QPropertyBindingPrivatePtr::T *const *lhs,
    const QPropertyBindingPrivatePtr *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(T *const &lhs, const QPropertyBindingPrivatePtr &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKPN9QtPrivate10RefCountedERK26QPropertyBindingPrivatePtr(
    QPropertyBindingPrivatePtr::T *const *lhs,
    const QPropertyBindingPrivatePtr *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QPropertyBindingPrivatePtr &lhs, const
//      std::nullptr_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK26QPropertyBindingPrivatePtrRKDn(
    const QPropertyBindingPrivatePtr *lhs) {
  return operator==(*lhs, nullptr);
}

//  bool operator!=(const QPropertyBindingPrivatePtr &lhs, const
//      std::nullptr_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK26QPropertyBindingPrivatePtrRKDn(
    const QPropertyBindingPrivatePtr *lhs) {
  return operator!=(*lhs, nullptr);
}

//  bool operator==(const std::nullptr_t &lhs, const
//      QPropertyBindingPrivatePtr &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKDnRK26QPropertyBindingPrivatePtr(
    const QPropertyBindingPrivatePtr *rhs) {
  return operator==(nullptr, *rhs);
}

//  bool operator!=(const std::nullptr_t &lhs, const
//      QPropertyBindingPrivatePtr &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKDnRK26QPropertyBindingPrivatePtr(
    const QPropertyBindingPrivatePtr *rhs) {
  return operator!=(nullptr, *rhs);
}
