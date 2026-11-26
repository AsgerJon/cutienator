//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qshadernode_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qshadernode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/quuid.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qshadernodeport_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qshaderformat_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <QtCore/QList>

//  Type Qt3DRender::QShaderNode::type() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderNode::Type ritual_ZNK10Qt3DRender11QShaderNode4typeEv(
    const Qt3DRender::QShaderNode *self) {
  return self->type();
}

//  QUuid Qt3DRender::QShaderNode::uuid() const
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZNK10Qt3DRender11QShaderNode4uuidEv(
    const Qt3DRender::QShaderNode *self) {
  return new QUuid(self->uuid());
}

//  void Qt3DRender::QShaderNode::setUuid(const QUuid &uuid)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QShaderNode7setUuidERK5QUuid(
    Qt3DRender::QShaderNode *self,
    const QUuid *uuid) {
  self->setUuid(*uuid);
}

//  QStringList Qt3DRender::QShaderNode::layers() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10Qt3DRender11QShaderNode6layersEv(
    const Qt3DRender::QShaderNode *self) {
  return new QList<QString>(self->layers());
}

//  void Qt3DRender::QShaderNode::setLayers(const QStringList &layers)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QShaderNode9setLayersERK5QListI7QStringE(
    Qt3DRender::QShaderNode *self,
    const QList<QString> *layers) {
  self->setLayers(*layers);
}

//  QList<QShaderNodePort> Qt3DRender::QShaderNode::ports() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QShaderNodePort> *ritual_ZNK10Qt3DRender11QShaderNode5portsEv(
    const Qt3DRender::QShaderNode *self) {
  return new QList<Qt3DRender::QShaderNodePort>(self->ports());
}

//  void Qt3DRender::QShaderNode::addPort(const QShaderNodePort &port)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QShaderNode7addPortERKNS_15QShaderNodePortE(
    Qt3DRender::QShaderNode *self,
    const Qt3DRender::QShaderNodePort *port) {
  self->addPort(*port);
}

//  void Qt3DRender::QShaderNode::removePort(const QShaderNodePort &port)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QShaderNode10removePortERKNS_15QShaderNodePortE(
    Qt3DRender::QShaderNode *self,
    const Qt3DRender::QShaderNodePort *port) {
  self->removePort(*port);
}

//  QStringList Qt3DRender::QShaderNode::parameterNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10Qt3DRender11QShaderNode14parameterNamesEv(
    const Qt3DRender::QShaderNode *self) {
  return new QList<QString>(self->parameterNames());
}

//  QVariant Qt3DRender::QShaderNode::parameter(const QString &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10Qt3DRender11QShaderNode9parameterERK7QString(
    const Qt3DRender::QShaderNode *self,
    const QString *name) {
  return new QVariant(self->parameter(*name));
}

//  void Qt3DRender::QShaderNode::setParameter(const QString &name, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QShaderNode12setParameterERK7QStringRK8QVariant(
    Qt3DRender::QShaderNode *self,
    const QString *name,
    const QVariant *value) {
  self->setParameter(*name, *value);
}

//  void Qt3DRender::QShaderNode::clearParameter(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QShaderNode14clearParameterERK7QString(
    Qt3DRender::QShaderNode *self,
    const QString *name) {
  self->clearParameter(*name);
}

//  void Qt3DRender::QShaderNode::addRule(const QShaderFormat &format, const
//      Rule &rule)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QShaderNode7addRuleERKNS_13QShaderFormatERKNS0_4RuleE(
    Qt3DRender::QShaderNode *self,
    const Qt3DRender::QShaderFormat *format,
    const Qt3DRender::QShaderNode::Rule *rule) {
  self->addRule(*format, *rule);
}

//  void Qt3DRender::QShaderNode::removeRule(const QShaderFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QShaderNode10removeRuleERKNS_13QShaderFormatE(
    Qt3DRender::QShaderNode *self,
    const Qt3DRender::QShaderFormat *format) {
  self->removeRule(*format);
}

//  QList<QShaderFormat> Qt3DRender::QShaderNode::availableFormats() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QShaderFormat> *ritual_ZNK10Qt3DRender11QShaderNode16availableFormatsEv(
    const Qt3DRender::QShaderNode *self) {
  return new QList<Qt3DRender::QShaderFormat>(self->availableFormats());
}

//  Rule Qt3DRender::QShaderNode::rule(const QShaderFormat &format) const
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderNode::Rule *ritual_ZNK10Qt3DRender11QShaderNode4ruleERKNS_13QShaderFormatE(
    const Qt3DRender::QShaderNode *self,
    const Qt3DRender::QShaderFormat *format) {
  return new Qt3DRender::QShaderNode::Rule(self->rule(*format));
}

//  Qt3DRender::QShaderNode::~QShaderNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QShaderNodeD1Ev(Qt3DRender::QShaderNode *self) {
  delete self;
}

//  a QList<Qt3DRender::QShaderNodePort> a ritual of Qt3DRender::QShaderNode
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QShaderNode__QList_Qt3DRender_QShaderNodePort(
    QList<Qt3DRender::QShaderNodePort> *self) {
  delete self;
}

//  a QList<Qt3DRender::QShaderFormat> a ritual of Qt3DRender::QShaderNode
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QShaderNode__QList_Qt3DRender_QShaderFormat(
    QList<Qt3DRender::QShaderFormat> *self) {
  delete self;
}
