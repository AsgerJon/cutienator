//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistaccessor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmllistaccessor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqmllistaccessor_p.h"
#include <private/qqmlmetatype_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmetasequence.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qurl.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmllistaccessor.cpp, line 16, as _ZN16QQmlListAccessorC1Ev
inline QQmlListAccessor::QQmlListAccessor()
: m_type(Invalid)
{
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistaccessor.cpp, line 21, as _ZN16QQmlListAccessorD1Ev
inline QQmlListAccessor::~QQmlListAccessor()
{
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistaccessor.cpp, line 25, as _ZNK16QQmlListAccessor4listEv
inline QVariant QQmlListAccessor::list() const
{
    return d;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistaccessor.cpp, line 30, as _ZN16QQmlListAccessor7setListERK8QVariant
inline void QQmlListAccessor::setList(const QVariant &v)
{
    d = v;

    // An incoming JS array as model is treated as a variant list, so we need to
    // convert it first with toVariant().
    QMetaType variantsType = d.metaType();
    if (variantsType == QMetaType::fromType<QJSValue>()) {
        d = d.value<QJSValue>().toVariant();
        variantsType = d.metaType();
    }

    if (!d.isValid()) {
        m_type = Invalid;
        return;
    }

    if (variantsType == QMetaType::fromType<QStringList>()) {
        m_type = StringList;
        return;
    }

    if (variantsType == QMetaType::fromType<QList<QUrl>>()) {
        m_type = UrlList;
        return;
    }

    if (variantsType == QMetaType::fromType<QVariantList>()) {
        m_type = VariantList;
        return;
    }

    if (variantsType == QMetaType::fromType<QList<QObject *>>()) {
        m_type = ObjectList;
        return;
    }

    if (variantsType.flags() & QMetaType::IsQmlList) {
        d = QVariant::fromValue(QQmlListReference(d));
        m_type = ListProperty;
        return;
    }

    if (variantsType == QMetaType::fromType<QQmlListReference>()) {
        m_type = ListProperty;
        return;
    }

    if (variantsType.flags() & QMetaType::PointerToQObject) {
        m_type = Instance;
        return;
    }

    if (int i = 0; [&](){bool ok = false; i = v.toInt(&ok); return ok;}()) {
        // Here we have to check for an upper limit, because down the line code might (well, will)
        // allocate memory depending on the number of elements. The upper limit cannot be INT_MAX:
        //      QList<QPointer<QQuickItem>> something;
        //      something.resize(count());
        // (See e.g. QQuickRepeater::regenerate())
        // This will allocate data along the lines of:
        //      sizeof(QPointer<QQuickItem>) * count() + QVector::headerSize
        // So, doing an approximate round-down-to-nice-number, we get:
        const int upperLimit = 100 * 1000 * 1000;

        if (i < 0) {
            qWarning("Model size of %d is less than 0", i);
            m_type = Invalid;
            return;
        }

        if (i > upperLimit) {
            qWarning("Model size of %d is bigger than the upper limit %d", i, upperLimit);
            m_type = Invalid;
            return;
        }

        m_type = Integer;
        d = i;
        return;
    }

    const QQmlType type = QQmlMetaType::qmlListType(variantsType);
    if (type.isSequentialContainer()) {
        m_metaSequence = type.listMetaSequence();
        m_type = m_metaSequence.valueMetaType().flags().testFlag(QMetaType::PointerToQObject)
                ? ObjectSequence
                : ValueSequence;
        return;
    }

    QMetaSequence::Iterable iterable;
    if (QMetaType::convert(
                variantsType, d.constData(),
                QMetaType::fromType<QMetaSequence::Iterable>(), &iterable)) {
        const QMetaSequence sequence = iterable.metaContainer();

        if (sequence.hasSize() && sequence.canGetValueAtIndex()) {
            // If the resulting iterable is useful for anything, use it.
            m_metaSequence = sequence;
            m_type = sequence.valueMetaType().flags().testFlag(QMetaType::PointerToQObject)
                    ? ObjectSequence
                    : ValueSequence;
            return;
        }

        if (sequence.hasConstIterator() && sequence.canGetValueAtConstIterator()) {
            // As a last resort, try to read the contents of the container via an iterator
            // and build a QVariantList from them.
            QVariantList variantList;
            for (auto it = iterable.constBegin(), end = iterable.constEnd(); it != end; ++it)
                variantList.push_back(*it);
            d = std::move(variantList);
            m_type = VariantList;
            return;
        }
    }

    m_type = Instance;
    return;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistaccessor.cpp, line 274, as _ZNK16QQmlListAccessor7isValidEv
inline bool QQmlListAccessor::isValid() const
{
    return m_type != Invalid;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistaccessor.cpp, line 151, as _ZNK16QQmlListAccessor5countEv
inline qsizetype QQmlListAccessor::count() const
{
    switch(m_type) {
    case StringList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QStringList>());
        return reinterpret_cast<const QStringList *>(d.constData())->size();
    case UrlList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QList<QUrl>>());
        return reinterpret_cast<const QList<QUrl> *>(d.constData())->size();
    case VariantList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QVariantList>());
        return reinterpret_cast<const QVariantList *>(d.constData())->size();
    case ObjectList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QList<QObject *>>());
        return reinterpret_cast<const QList<QObject *> *>(d.constData())->size();
    case ListProperty:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QQmlListReference>());
        return reinterpret_cast<const QQmlListReference *>(d.constData())->count();
    case ValueSequence:
    case ObjectSequence:
        Q_ASSERT(m_metaSequence != QMetaSequence());
        return m_metaSequence.size(d.constData());
    case Instance:
        return 1;
    case Integer:
        return *reinterpret_cast<const int *>(d.constData());
    case Invalid:
        return 0;
    }
    Q_UNREACHABLE_RETURN(0);
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistaccessor.cpp, line 183, as _ZNK16QQmlListAccessor2atEx
inline QVariant QQmlListAccessor::at(qsizetype idx) const
{
    Q_ASSERT(idx >= 0 && idx < count());
    switch(m_type) {
    case StringList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QStringList>());
        return QVariant::fromValue(reinterpret_cast<const QStringList *>(d.constData())->at(idx));
    case UrlList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QList<QUrl>>());
        return QVariant::fromValue(reinterpret_cast<const QList<QUrl> *>(d.constData())->at(idx));
    case VariantList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QVariantList>());
        return reinterpret_cast<const QVariantList *>(d.constData())->at(idx);
    case ObjectList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QList<QObject *>>());
        return QVariant::fromValue(reinterpret_cast<const QList<QObject *> *>(d.constData())->at(idx));
    case ListProperty:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QQmlListReference>());
        return QVariant::fromValue(reinterpret_cast<const QQmlListReference *>(d.constData())->at(idx));
    case ValueSequence:
    case ObjectSequence: {
        Q_ASSERT(m_metaSequence != QMetaSequence());
        QVariant result;
        const QMetaType valueMetaType = m_metaSequence.valueMetaType();
        if (valueMetaType == QMetaType::fromType<QVariant>()) {
            m_metaSequence.valueAtIndex(d.constData(), idx, &result);
        } else {
            result = QVariant(valueMetaType);
            m_metaSequence.valueAtIndex(d.constData(), idx, result.data());
        }
        return result;
    }
    case Instance:
        return d;
    case Integer:
        return QVariant(idx);
    case Invalid:
        return QVariant();
    }
    Q_UNREACHABLE_RETURN(QVariant());
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistaccessor.cpp, line 225, as _ZN16QQmlListAccessor3setExRK8QVariant
inline void QQmlListAccessor::set(qsizetype idx, const QVariant &value)
{
    Q_ASSERT(idx >= 0 && idx < count());
    switch (m_type) {
    case StringList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QStringList>());
        (*static_cast<QStringList *>(d.data()))[idx] = value.toString();
        break;
    case UrlList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QList<QUrl>>());
        (*static_cast<QList<QUrl> *>(d.data()))[idx] = value.value<QUrl>();
        break;
    case VariantList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QVariantList>());
        (*static_cast<QVariantList *>(d.data()))[idx] = value;
        break;
    case ObjectList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QList<QObject *>>());
        (*static_cast<QList<QObject *> *>(d.data()))[idx] = value.value<QObject *>();
        break;
    case ListProperty:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QQmlListReference>());
        static_cast<QQmlListReference *>(d.data())->replace(idx, value.value<QObject *>());
        break;
    case ValueSequence:
    case ObjectSequence: {
        Q_ASSERT(m_metaSequence != QMetaSequence());
        const QMetaType valueMetaType = m_metaSequence.valueMetaType();
        if (valueMetaType == QMetaType::fromType<QVariant>()) {
            m_metaSequence.setValueAtIndex(d.data(), idx, &value);
        } else if (valueMetaType == value.metaType()) {
            m_metaSequence.setValueAtIndex(d.data(), idx, value.constData());
        } else {
            QVariant converted = value;
            converted.convert(valueMetaType);
            m_metaSequence.setValueAtIndex(d.data(), idx, converted.constData());
        }
        break;
    }
    case Instance:
        d = value;
        break;
    case Integer:
        break;;
    case Invalid:
        break;
    }
}
//  -----------------------------------------------------------------------

//  QQmlListAccessor::QQmlListAccessor()
extern "C" Q_DECL_EXPORT
QQmlListAccessor *ritual_ZN16QQmlListAccessorC1Ev() {
  return new QQmlListAccessor();
}

//  QQmlListAccessor::~QQmlListAccessor()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlListAccessorD1Ev(QQmlListAccessor *self) {
  delete self;
}

//  QVariant QQmlListAccessor::list() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QQmlListAccessor4listEv(const QQmlListAccessor *self) {
  return new QVariant(self->list());
}

//  void QQmlListAccessor::setList(const QVariant &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlListAccessor7setListERK8QVariant(
    QQmlListAccessor *self,
    const QVariant *a0) {
  self->setList(*a0);
}

//  bool QQmlListAccessor::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlListAccessor7isValidEv(const QQmlListAccessor *self) {
  return self->isValid();
}

//  qsizetype QQmlListAccessor::count() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK16QQmlListAccessor5countEv(
    const QQmlListAccessor *self) {
  return self->count();
}

//  QVariant QQmlListAccessor::at(qsizetype a0) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QQmlListAccessor2atEx(
    const QQmlListAccessor *self,
    qsizetype a0) {
  return new QVariant(self->at(a0));
}

//  void QQmlListAccessor::set(qsizetype a0, const QVariant &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlListAccessor3setExRK8QVariant(
    QQmlListAccessor *self,
    qsizetype a0,
    const QVariant *a1) {
  self->set(a0, *a1);
}

//  Type QQmlListAccessor::type() const
extern "C" Q_DECL_EXPORT
QQmlListAccessor::Type ritual_ZNK16QQmlListAccessor4typeEv(
    const QQmlListAccessor *self) {
  return self->type();
}
