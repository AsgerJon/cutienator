//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_list_model)
#if QT_CONFIG(qml_list_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmllistmodel_p_p.h>
#include <QtQmlModels/private/qqmllistmodelworkeragent_p.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtQml/private/qqmlcustomparser_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmljsast_p.h>
#include <QtQml/private/qqmljsengine_p.h>
#include <QtQml/private/qqmllistwrapper_p.h>
#include <QtQml/private/qqmlnotifier_p.h>
#include <QtQml/private/qqmlopenmetaobject_p.h>
#include <QtQml/private/qv4alloca_p.h>
#include <QtQml/private/qv4dateobject_p.h>
#include <QtQml/private/qv4lookup_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#include <QtQml/private/qv4qmlcontext_p.h>
#include <QtQml/private/qv4sequenceobject_p.h>
#include <QtQml/private/qv4urlobject_p.h>
#include <QtQml/qqmlcontext.h>
#include <QtQml/qqmlinfo.h>
#include <QtCore/qdebug.h>
#include <QtCore/qstack.h>
#include <QtCore/QXmlStreamReader>
#include <QtCore/qdatetime.h>
#include <QtCore/QScopedValueRollback>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 264, as _ZN19StringOrTranslationD1Ev
inline StringOrTranslation::~StringOrTranslation()
{
    clear();
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 269, as _ZN19StringOrTranslation9setStringERK7QString
inline void StringOrTranslation::setString(const QString &s)
{
    clear();
    if (s.isEmpty())
        return;
    QString::DataPointer dataPointer = s.data_ptr();
    arrayData = dataPointer.d_ptr();
    stringData = dataPointer.data();
    stringSize = dataPointer.size;
    if (arrayData)
        arrayData->ref();
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 282, as _ZN19StringOrTranslation14setTranslationEPKN3QV412CompiledData7BindingE
inline void StringOrTranslation::setTranslation(const QV4::CompiledData::Binding *binding)
{
    clear();
    this->binding = binding;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 288, as _ZNK19StringOrTranslation8toStringEPK13QQmlListModel
inline QString StringOrTranslation::toString(const QQmlListModel *owner) const
{
    if (stringSize) {
        if (arrayData)
            arrayData->ref();
        return QString(QStringPrivate(arrayData, stringData, stringSize));
    }
    if (!owner)
        return QString();
    return owner->m_compilationUnit->bindingValueAsString(binding);
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 300, as _ZNK19StringOrTranslation8asStringEv
inline QString StringOrTranslation::asString() const
{
    if (!arrayData)
        return QString();
    arrayData->ref();
    return QString(QStringPrivate(arrayData, stringData, stringSize));
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 308, as _ZN19StringOrTranslation5clearEv
inline void StringOrTranslation::clear()
{
    if (arrayData && !arrayData->deref())
        QTypedArrayData<ushort>::deallocate(arrayData);
    arrayData = nullptr;
    stringData = nullptr;
    stringSize = 0;
    binding = nullptr;
}
//  -----------------------------------------------------------------------

//  StringOrTranslation::~StringOrTranslation()
extern "C" Q_DECL_EXPORT
void ritual_ZN19StringOrTranslationD1Ev(StringOrTranslation *self) {
  delete self;
}

//  bool StringOrTranslation::isSet() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19StringOrTranslation5isSetEv(
    const StringOrTranslation *self) {
  return self->isSet();
}

//  bool StringOrTranslation::isTranslation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19StringOrTranslation13isTranslationEv(
    const StringOrTranslation *self) {
  return self->isTranslation();
}

//  void StringOrTranslation::setString(const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN19StringOrTranslation9setStringERK7QString(
    StringOrTranslation *self,
    const QString *s) {
  self->setString(*s);
}

//  void StringOrTranslation::setTranslation(const QV4::CompiledData::Binding
//      *binding)
extern "C" Q_DECL_EXPORT
void ritual_ZN19StringOrTranslation14setTranslationEPKN3QV412CompiledData7BindingE(
    StringOrTranslation *self,
    const QV4::CompiledData::Binding *binding) {
  self->setTranslation(binding);
}

//  QString StringOrTranslation::toString(const QQmlListModel *owner) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19StringOrTranslation8toStringEPK13QQmlListModel(
    const StringOrTranslation *self,
    const QQmlListModel *owner) {
  return new QString(self->toString(owner));
}

//  QString StringOrTranslation::asString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19StringOrTranslation8asStringEv(
    const StringOrTranslation *self) {
  return new QString(self->asString());
}

//  void StringOrTranslation::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN19StringOrTranslation5clearEv(StringOrTranslation *self) {
  self->clear();
}

#endif  // QT_CONFIG(qml_list_model)
#endif  // QT_CONFIG(qml_list_model)
