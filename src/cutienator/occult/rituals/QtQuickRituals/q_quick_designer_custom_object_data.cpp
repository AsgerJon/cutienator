//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdesignercustomobjectdata_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_designer)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdesignercustomobjectdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlanybinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickdesignersupportmetainfo_p.h>
#include <QtQuick/private/qquickdesignersupportproperties_p.h>
#include <QtQuick/private/qquickdesignercustomobjectdata_p.h>
#include <QtCore/QGlobalStatic>
#include <QtQml/QQmlContext>
#include <QtQml/QQmlEngine>
#include <QtQml/private/qqmlanybinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/designer/qquickdesignercustomobjectdata.cpp, line 112, as _ZN30QQuickDesignerCustomObjectData19populateResetHashesEv
inline void QQuickDesignerCustomObjectData::populateResetHashes()
{
    const QQuickDesignerSupport::PropertyNameList propertyNameList =
            QQuickDesignerSupportProperties::propertyNameListForWritableProperties(object());

    const QMetaObject *mo = object()->metaObject();
    QByteArrayList deferredPropertyNames;
    const int namesIndex = mo->indexOfClassInfo("DeferredPropertyNames");
    if (namesIndex != -1) {
        QMetaClassInfo classInfo = mo->classInfo(namesIndex);
        deferredPropertyNames = QByteArray(classInfo.value()).split(',');
    }

    for (const QQuickDesignerSupport::PropertyName &propertyName : propertyNameList) {

        if (deferredPropertyNames.contains(propertyName))
            continue;

        QQmlProperty property(object(), QString::fromUtf8(propertyName), QQmlEngine::contextForObject(object()));

        auto binding = QQmlAnyBinding::ofProperty(property);

        if (binding) {
            m_resetBindingHash.insert(propertyName, binding);
        } else if (property.isWritable()) {
            m_resetValueHash.insert(propertyName, property.read());
        }
    }
}

//  from ../qtdeclarative/src/quick/designer/qquickdesignercustomobjectdata.cpp, line 142, as _ZNK30QQuickDesignerCustomObjectData6objectEv
inline QObject *QQuickDesignerCustomObjectData::object() const
{
    return m_object;
}

//  from ../qtdeclarative/src/quick/designer/qquickdesignercustomobjectdata.cpp, line 147, as _ZNK30QQuickDesignerCustomObjectData13getResetValueERK10QByteArray
inline QVariant QQuickDesignerCustomObjectData::getResetValue(const QQuickDesignerSupport::PropertyName &propertyName) const
{
    return m_resetValueHash.value(propertyName);
}

//  from ../qtdeclarative/src/quick/designer/qquickdesignercustomobjectdata.cpp, line 152, as _ZN30QQuickDesignerCustomObjectData15doResetPropertyEP11QQmlContextRK10QByteArray
inline void QQuickDesignerCustomObjectData::doResetProperty(QQmlContext *context, const QQuickDesignerSupport::PropertyName &propertyName)
{
    QQmlProperty property(object(), QString::fromUtf8(propertyName), context);

    if (!property.isValid())
        return;

    // remove existing binding
    QQmlAnyBinding::takeFrom(property);


    if (hasValidResetBinding(propertyName)) {
        QQmlAnyBinding binding = getResetBinding(propertyName);
        binding.installOn(property);

        if (binding.isAbstractPropertyBinding()) {
            // for new style properties, we will evaluate during setBinding anyway
            static_cast<QQmlBinding *>(binding.asAbstractBinding())->update();
        }

    } else if (property.isResettable()) {
        property.reset();
    } else if (property.propertyTypeCategory() == QQmlProperty::List) {
        QQmlListReference list = qvariant_cast<QQmlListReference>(property.read());

        if (!QQuickDesignerSupportProperties::hasFullImplementedListInterface(list)) {
            qWarning() << "Property list interface not fully implemented for Class " << property.property().typeName() << " in property " << property.name() << "!";
            return;
        }

        list.clear();
    } else if (property.isWritable()) {
        if (property.read() == getResetValue(propertyName))
            return;

        property.write(getResetValue(propertyName));
    }
}

//  from ../qtdeclarative/src/quick/designer/qquickdesignercustomobjectdata.cpp, line 191, as _ZNK30QQuickDesignerCustomObjectData20hasValidResetBindingERK10QByteArray
inline bool QQuickDesignerCustomObjectData::hasValidResetBinding(const QQuickDesignerSupport::PropertyName &propertyName) const
{
    return m_resetBindingHash.contains(propertyName) &&  m_resetBindingHash.value(propertyName);
}

//  from ../qtdeclarative/src/quick/designer/qquickdesignercustomobjectdata.cpp, line 196, as _ZNK30QQuickDesignerCustomObjectData15getResetBindingERK10QByteArray
inline QQmlAnyBinding QQuickDesignerCustomObjectData::getResetBinding(const QQuickDesignerSupport::PropertyName &propertyName) const
{
    return m_resetBindingHash.value(propertyName);
}

//  from ../qtdeclarative/src/quick/designer/qquickdesignercustomobjectdata.cpp, line 201, as _ZNK30QQuickDesignerCustomObjectData21hasBindingForPropertyEP11QQmlContextRK10QByteArrayPb
inline bool QQuickDesignerCustomObjectData::hasBindingForProperty(QQmlContext *context,
                                                     const QQuickDesignerSupport::PropertyName &propertyName,
                                                     bool *hasChanged) const
{
    if (QQuickDesignerSupportProperties::isPropertyBlackListed(propertyName))
        return false;

    QQmlProperty property(object(), QString::fromUtf8(propertyName), context);

    bool hasBinding = QQmlAnyBinding::ofProperty(property);

    if (hasChanged) {
        *hasChanged = hasBinding != m_hasBindingHash.value(propertyName, false);
        if (*hasChanged)
            m_hasBindingHash.insert(propertyName, hasBinding);
    }

    return hasBinding;
}

//  from ../qtdeclarative/src/quick/designer/qquickdesignercustomobjectdata.cpp, line 252, as _ZN30QQuickDesignerCustomObjectData29keepBindingFromGettingDeletedEP11QQmlContextRK10QByteArray
inline void QQuickDesignerCustomObjectData::keepBindingFromGettingDeleted(QQmlContext *context,
                                                             const QQuickDesignerSupport::PropertyName &propertyName)
{
    //Refcounting is taking care
    Q_UNUSED(context);
    Q_UNUSED(propertyName);
}
//  -----------------------------------------------------------------------

//  void QQuickDesignerCustomObjectData::populateResetHashes()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickDesignerCustomObjectData19populateResetHashesEv(
    QQuickDesignerCustomObjectData *self) {
  self->populateResetHashes();
}

//  QObject *QQuickDesignerCustomObjectData::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK30QQuickDesignerCustomObjectData6objectEv(
    const QQuickDesignerCustomObjectData *self) {
  return self->object();
}

//  QVariant QQuickDesignerCustomObjectData::getResetValue(const
//      QQuickDesignerSupport::PropertyName &propertyName) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK30QQuickDesignerCustomObjectData13getResetValueERK10QByteArray(
    const QQuickDesignerCustomObjectData *self,
    const QByteArray *propertyName) {
  return new QVariant(self->getResetValue(*propertyName));
}

//  void QQuickDesignerCustomObjectData::doResetProperty(QQmlContext
//      *context, const QQuickDesignerSupport::PropertyName &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickDesignerCustomObjectData15doResetPropertyEP11QQmlContextRK10QByteArray(
    QQuickDesignerCustomObjectData *self,
    QQmlContext *context,
    const QByteArray *propertyName) {
  self->doResetProperty(context, *propertyName);
}

//  bool QQuickDesignerCustomObjectData::hasValidResetBinding(const
//      QQuickDesignerSupport::PropertyName &propertyName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQuickDesignerCustomObjectData20hasValidResetBindingERK10QByteArray(
    const QQuickDesignerCustomObjectData *self,
    const QByteArray *propertyName) {
  return self->hasValidResetBinding(*propertyName);
}

//  QQmlAnyBinding QQuickDesignerCustomObjectData::getResetBinding(const
//      QQuickDesignerSupport::PropertyName &propertyName) const
extern "C" Q_DECL_EXPORT
QQmlAnyBinding *ritual_ZNK30QQuickDesignerCustomObjectData15getResetBindingERK10QByteArray(
    const QQuickDesignerCustomObjectData *self,
    const QByteArray *propertyName) {
  return new QQmlAnyBinding(self->getResetBinding(*propertyName));
}

//  bool QQuickDesignerCustomObjectData::hasBindingForProperty(QQmlContext
//      *context, const QQuickDesignerSupport::PropertyName &propertyName,
//      bool *hasChanged) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQuickDesignerCustomObjectData21hasBindingForPropertyEP11QQmlContextRK10QByteArrayPb(
    const QQuickDesignerCustomObjectData *self,
    QQmlContext *context,
    const QByteArray *propertyName,
    bool *hasChanged) {
  return self->hasBindingForProperty(context, *propertyName, hasChanged);
}

//  void
//      QQuickDesignerCustomObjectData::keepBindingFromGettingDeleted(QQmlCon
//      text *context, const QQuickDesignerSupport::PropertyName
//      &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickDesignerCustomObjectData29keepBindingFromGettingDeletedEP11QQmlContextRK10QByteArray(
    QQuickDesignerCustomObjectData *self,
    QQmlContext *context,
    const QByteArray *propertyName) {
  self->keepBindingFromGettingDeleted(context, *propertyName);
}

//  QQuickDesignerCustomObjectData::~QQuickDesignerCustomObjectData()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickDesignerCustomObjectDataD1Ev(
    QQuickDesignerCustomObjectData *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_designer)
