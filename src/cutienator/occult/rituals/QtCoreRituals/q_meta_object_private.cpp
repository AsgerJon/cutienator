//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmetaobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmetaobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearrayview.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/QSpan>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/private/qmetaobject_p.h>
#include <QtCore/qmetatype.h>
#include <QtCore/private/qmetatype_p.h>
#include <QtCore/qobject.h>
#include <QtCore/private/qobject_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qspan.h>
#include <QtCore/qvariant.h>
#include <QtCore/qthread.h>
#include <QtCore/private/qthread_p.h>
#if QT_CONFIG(thread)
#include <QtCore/private/qlatch_p.h>
#endif
#include <QtCore/private/qmetaobject_moc_p.h>
#include <ctype.h>
#include <memory>
#include <cstring>
#include <QtCore/qtconfigmacros.h>
#include <QtCore/qobject.h>
#include <QtCore/private/qobject_p.h>
#include <QtCore/private/qobject_p_p.h>
#include <QtCore/private/qmetaobject_p.h>
#include <QtCore/private/qtclasshelper_p.h>
#include <QtCore/qspan.h>
#include <QtCore/qabstracteventdispatcher.h>
#include <QtCore/private/qabstracteventdispatcher_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/private/qcoreapplication_p.h>
#include <QtCore/private/qcoreevent_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#if QT_CONFIG(regularexpression)
#  include <QtCore/qregularexpression.h>
#endif
#include <QtCore/qthread.h>
#include <QtCore/private/qthread_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qscopeguard.h>
#include <QtCore/qset.h>
#if QT_CONFIG(thread)
#include <QtCore/private/qlatch_p.h>
#endif
#include <QtCore/private/qorderedmutexlocker_p.h>
#include <QtCore/private/qhooks_p.h>
#include <new>
#include <mutex>
#include <memory>
#include <optional>
#include <iterator>
#include <ctype.h>
#include <limits.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/kernel/qmetaobject.cpp, line 124, as local:qmetaobject.cpp:priv
static inline const QMetaObjectPrivate *priv(const uint* data)
{ return reinterpret_cast<const QMetaObjectPrivate*>(data); }

//  from src/corelib/kernel/qmetaobject.cpp, line 134, as local:qmetaobject.cpp:stringDataView
static inline QByteArrayView stringDataView(const QMetaObject *mo, int index)
{
    Q_ASSERT(priv(mo->d.data)->revision >= 7);
    uint offset = mo->d.stringdata[2*index];
    uint length = mo->d.stringdata[2*index + 1];
    const char *string = reinterpret_cast<const char *>(mo->d.stringdata) + offset;
    return {string, qsizetype(length)};
}

//  from src/corelib/kernel/qmetaobject.cpp, line 1369, as local:qmetaobject.cpp:trimSpacesFromLeft
static const char *trimSpacesFromLeft(QByteArrayView in)
{
    return std::find_if_not(in.begin(), in.end(), is_space);
}

//  from src/corelib/kernel/qmetaobject.cpp, line 1374, as local:qmetaobject.cpp:trimSpacesFromRight
static QByteArrayView trimSpacesFromRight(QByteArrayView in)
{
    auto rit = std::find_if_not(in.rbegin(), in.rend(), is_space);
    in = in.first(rit.base() - in.begin());
    return in;
}

//  from src/corelib/kernel/qobject.cpp, line 228, as local:qobject.cpp:computeOffsets
static void computeOffsets(const QMetaObject *metaobject, int *signalOffset, int *methodOffset)
{
    *signalOffset = *methodOffset = 0;
    const QMetaObject *m = metaobject->d.superdata;
    while (m) {
        const QMetaObjectPrivate *d = QMetaObjectPrivate::get(m);
        *methodOffset += d->methodCount;
        Q_ASSERT(d->revision >= 4);
        *signalOffset += d->signalCount;
        m = m->d.superdata;
    }
}

//  from src/corelib/kernel/qmetaobject.cpp, line 717, as _ZN18QMetaObjectPrivate21indexOfMethodRelativeEPPK11QMetaObject14QByteArrayView5QSpanIK13QArgumentTypeLm18446744073709551615EEN11QMetaMethod10MethodTypeE
inline int QMetaObjectPrivate::indexOfMethodRelative(const QMetaObject **baseObject,
                                        QByteArrayView name,
                                        QSpan<const QArgumentType> types,
                                        QMetaMethod::MethodType what)
{
    for (const QMetaObject *m = *baseObject; m; m = m->d.superdata) {
        Q_ASSERT(priv(m->d.data)->revision >= 7);
        int i = 0;
        int end = 0;
        switch (what) {
        case QMetaMethod::Signal:
            i = priv(m->d.data)->signalCount - 1;
            break;
        case QMetaMethod::Slot:
            i = priv(m->d.data)->methodCount - 1;
            end = priv(m->d.data)->signalCount;
            break;
        case QMetaMethod::Method:
            i = priv(m->d.data)->methodCount - 1;
            break;
        case QMetaMethod::Constructor:
            Q_UNREACHABLE_RETURN(-1);
        }

        // Is iterating backwards here significant?
        for (; i >= end; --i) {
            auto data = QMetaMethod::fromRelativeMethodIndex(m, i);
            if (methodMatch(m, data, name, types)) {
                if (QT_VERSION >= QT_VERSION_CHECK(7, 0, 0)
                    && what == QMetaMethod::Slot && data.methodType() != QMetaMethod::Slot) {
                    return -1;
                }
                *baseObject = m;
                return i;
            }
        }
    }
    return -1;
}

//  from src/corelib/kernel/qmetaobject.cpp, line 1150, as _ZN18QMetaObjectPrivate17indexOfEnumeratorEPK11QMetaObject14QByteArrayViewNS_5WhichE
inline int QMetaObjectPrivate::indexOfEnumerator(const QMetaObject *m, QByteArrayView name, Which which)
{
    while (m) {
        const QMetaObjectPrivate *d = priv(m->d.data);
        for (int i = 0; i < d->enumeratorCount; ++i) {
            const QMetaEnum e(m, i);
            const quint32 id = which == Which::Name ? e.data.name() : e.data.alias();
            QByteArrayView prop = stringDataView(m, id);
            if (name == prop) {
                i += m->enumeratorOffset();
                return i;
            }
        }
        m = m->d.superdata;
    }
    return -1;
}

//  from src/corelib/kernel/qmetaobject.cpp, line 4633, as _ZN18QMetaObjectPrivate13originalCloneEPK11QMetaObjecti
inline int QMetaObjectPrivate::originalClone(const QMetaObject *mobj, int local_method_index)
{
    Q_ASSERT(local_method_index < get(mobj)->methodCount);
    while (QMetaMethod::fromRelativeMethodIndex(mobj, local_method_index).data.flags() & MethodCloned) {
        Q_ASSERT(local_method_index > 0);
        --local_method_index;
    }
    return local_method_index;
}

//  from src/corelib/kernel/qmetaobject.cpp, line 1140, as _ZN18QMetaObjectPrivate17indexOfEnumeratorEPK11QMetaObject14QByteArrayView
inline int QMetaObjectPrivate::indexOfEnumerator(const QMetaObject *m, QByteArrayView name)
{
    using W = QMetaObjectPrivate::Which;
    for (auto which : { W::Name, W::Alias }) {
        if (int index = indexOfEnumerator(m, name, which); index != -1)
            return index;
    }
    return -1;
}

//  from src/corelib/kernel/qmetaobject.cpp, line 1062, as _ZN18QMetaObjectPrivate16checkConnectArgsE5QSpanIK13QArgumentTypeLm18446744073709551615EES3_
inline bool QMetaObjectPrivate::checkConnectArgs(QSpan<const QArgumentType> signalTypes,
                                          QSpan<const QArgumentType> methodTypes)
{
    const qsizetype methodArgc = methodTypes.size();
    if (signalTypes.size() >= methodArgc) {
        signalTypes = signalTypes.first(methodArgc);
        return std::equal(signalTypes.begin(), signalTypes.end(),
                          methodTypes.begin(), methodTypes.end());
    }
    return false;
}

//  from src/corelib/kernel/qmetaobject.cpp, line 4652, as _ZN18QMetaObjectPrivate31parameterTypeNamesFromSignatureE14QByteArrayViewR15QVarLengthArrayIS0_Lx10EE
inline QByteArrayView
QMetaObjectPrivate::parameterTypeNamesFromSignature(QByteArrayView sig,
                                                    QVarLengthArray<QByteArrayView, 10> &typeNames)
{
    const char *signature = static_cast<const char *>(memchr(sig.begin(), '(', sig.size()));
    if (!signature)
        return {};
    auto name = QByteArrayView{sig.begin(), signature};
    ++signature; // skip '('
    if (!sig.endsWith(')'))
        return {};
    const char *end = sig.end() - 1; // exclude ')'
    while (signature != end) {
        if (*signature == ',')
            ++signature;
        const char *begin = signature;
        int level = 0;
        while (signature != end && (level > 0 || *signature != ',')) {
            if (*signature == '<')
                ++level;
            else if (*signature == '>')
                --level;
            ++signature;
        }
        typeNames.append(QByteArrayView{begin, signature - begin});
    }
    return name;
}

//  from src/corelib/kernel/qobject.cpp, line 3002, as _ZN18QMetaObjectPrivate13memberIndexesEPK7QObjectRK11QMetaMethodPiS6_
inline void QMetaObjectPrivate::memberIndexes(const QObject *obj,
                                       const QMetaMethod &member,
                                       int *signalIndex, int *methodIndex)
{
    *signalIndex = -1;
    *methodIndex = -1;
    if (!obj || !member.mobj)
        return;
    const QMetaObject *m = obj->metaObject();
    // Check that member is member of obj class
    while (m != nullptr && m != member.mobj)
        m = m->d.superdata;
    if (!m)
        return;
    *signalIndex = *methodIndex = member.relativeMethodIndex();

    int signalOffset;
    int methodOffset;
    computeOffsets(m, &signalOffset, &methodOffset);

    *methodIndex += methodOffset;
    if (member.methodType() == QMetaMethod::Signal) {
        *signalIndex = originalClone(m, *signalIndex);
        *signalIndex += signalOffset;
    } else {
        *signalIndex = -1;
    }
}
//  -----------------------------------------------------------------------

//  const QMetaObjectPrivate *QMetaObjectPrivate::get(const QMetaObject
//      *metaobject)
extern "C" Q_DECL_EXPORT
const QMetaObjectPrivate *ritual_ZN18QMetaObjectPrivate3getEPK11QMetaObject(
    const QMetaObject *metaobject) {
  return QMetaObjectPrivate::get(metaobject);
}

//  int QMetaObjectPrivate::originalClone(const QMetaObject *obj, int
//      local_method_index)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QMetaObjectPrivate13originalCloneEPK11QMetaObjecti(
    const QMetaObject *obj,
    int local_method_index) {
  return QMetaObjectPrivate::originalClone(obj, local_method_index);
}

//  int QMetaObjectPrivate::indexOfEnumerator(const QMetaObject *m,
//      QByteArrayView name)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QMetaObjectPrivate17indexOfEnumeratorEPK11QMetaObject14QByteArrayView(
    const QMetaObject *m,
    const QByteArrayView *name) {
  return QMetaObjectPrivate::indexOfEnumerator(m, *name);
}

//  QMetaMethod QMetaObjectPrivate::signal(const QMetaObject *m, int
//      signal_index)
extern "C" Q_DECL_EXPORT
QMetaMethod *ritual_ZN18QMetaObjectPrivate6signalEPK11QMetaObjecti(
    const QMetaObject *m,
    int signal_index) {
  return new QMetaMethod(QMetaObjectPrivate::signal(m, signal_index));
}

//  int QMetaObjectPrivate::signalOffset(const QMetaObject *m)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QMetaObjectPrivate12signalOffsetEPK11QMetaObject(
    const QMetaObject *m) {
  return QMetaObjectPrivate::signalOffset(m);
}

//  int QMetaObjectPrivate::absoluteSignalCount(const QMetaObject *m)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QMetaObjectPrivate19absoluteSignalCountEPK11QMetaObject(
    const QMetaObject *m) {
  return QMetaObjectPrivate::absoluteSignalCount(m);
}

//  int QMetaObjectPrivate::signalIndex(const QMetaMethod &m)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QMetaObjectPrivate11signalIndexERK11QMetaMethod(
    const QMetaMethod *m) {
  return QMetaObjectPrivate::signalIndex(*m);
}

//  bool QMetaObjectPrivate::checkConnectArgs(QSpan<const QArgumentType>
//      signalTypes, QSpan<const QArgumentType> methodTypes)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QMetaObjectPrivate16checkConnectArgsE5QSpanIK13QArgumentTypeLm18446744073709551615EES3_(
    const QSpan<const QArgumentType> *signalTypes,
    const QSpan<const QArgumentType> *methodTypes) {
  return QMetaObjectPrivate::checkConnectArgs(*signalTypes, *methodTypes);
}

//  QByteArrayView
//      QMetaObjectPrivate::parameterTypeNamesFromSignature(QByteArrayView
//      signature, QVarLengthArray<QByteArrayView, 10> &typeNames)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN18QMetaObjectPrivate31parameterTypeNamesFromSignatureE14QByteArrayViewR15QVarLengthArrayIS0_Lx10EE(
    const QByteArrayView *signature,
    QVarLengthArray<QByteArrayView, 10> *typeNames) {
  return new QByteArrayView(
      QMetaObjectPrivate::parameterTypeNamesFromSignature(
          *signature,
          *typeNames));
}

#if !defined(QT_NO_QOBJECT)
//  void QMetaObjectPrivate::memberIndexes(const QObject *obj, const
//      QMetaMethod &member, int *signalIndex, int *methodIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaObjectPrivate13memberIndexesEPK7QObjectRK11QMetaMethodPiS6_(
    const QObject *obj,
    const QMetaMethod *member,
    int *signalIndex,
    int *methodIndex) {
  QMetaObjectPrivate::memberIndexes(obj, *member, signalIndex, methodIndex);
}
#endif  // !defined(QT_NO_QOBJECT)

//  QMetaMethod QMetaObjectPrivate::firstMethod(const QMetaObject
//      *baseObject, QByteArrayView name)
extern "C" Q_DECL_EXPORT
QMetaMethod *ritual_ZN18QMetaObjectPrivate11firstMethodEPK11QMetaObject14QByteArrayView(
    const QMetaObject *baseObject,
    const QByteArrayView *name) {
  return new QMetaMethod(QMetaObjectPrivate::firstMethod(baseObject, *name));
}

//  QMetaObjectPrivate::~QMetaObjectPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaObjectPrivateD1Ev(QMetaObjectPrivate *self) {
  delete self;
}
