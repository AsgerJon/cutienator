//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/formbuilderextra_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/formbuilderextra_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpalette.h>
#include <QtGui/qbrush.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qlist.h>

//  QFormBuilderExtra::QFormBuilderExtra()
extern "C" Q_DECL_EXPORT
QFormBuilderExtra *ritual_ZN17QFormBuilderExtraC1Ev() {
  return new QFormBuilderExtra();
}

//  QFormBuilderExtra::~QFormBuilderExtra()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFormBuilderExtraD1Ev(QFormBuilderExtra *self) {
  delete self;
}

//  void QFormBuilderExtra::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFormBuilderExtra5clearEv(QFormBuilderExtra *self) {
  self->clear();
}

//  DomUI *QFormBuilderExtra::readUi(QIODevice *dev)
extern "C" Q_DECL_EXPORT
DomUI *ritual_ZN17QFormBuilderExtra6readUiEP9QIODevice(
    QFormBuilderExtra *self,
    QIODevice *dev) {
  return self->readUi(dev);
}

//  QString QFormBuilderExtra::msgInvalidUiFile()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QFormBuilderExtra16msgInvalidUiFileEv() {
  return new QString(QFormBuilderExtra::msgInvalidUiFile());
}

//  bool QFormBuilderExtra::applyPropertyInternally(QObject *o, const QString
//      &propertyName, const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QFormBuilderExtra23applyPropertyInternallyEP7QObjectRK7QStringRK8QVariant(
    QFormBuilderExtra *self,
    QObject *o,
    const QString *propertyName,
    const QVariant *value) {
  return self->applyPropertyInternally(o, *propertyName, *value);
}

//  void QFormBuilderExtra::applyInternalProperties() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QFormBuilderExtra23applyInternalPropertiesEv(
    const QFormBuilderExtra *self) {
  self->applyInternalProperties();
}

//  bool QFormBuilderExtra::applyBuddy(const QString &buddyName, BuddyMode
//      applyMode, QLabel *label)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QFormBuilderExtra10applyBuddyERK7QStringNS_9BuddyModeEP6QLabel(
    const QString *buddyName,
    QFormBuilderExtra::BuddyMode applyMode,
    QLabel *label) {
  return QFormBuilderExtra::applyBuddy(*buddyName, applyMode, label);
}

//  bool QFormBuilderExtra::parentWidgetIsSet() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QFormBuilderExtra17parentWidgetIsSetEv(
    const QFormBuilderExtra *self) {
  return self->parentWidgetIsSet();
}

//  void QFormBuilderExtra::setProcessingLayoutWidget(bool processing)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFormBuilderExtra25setProcessingLayoutWidgetEb(
    QFormBuilderExtra *self,
    bool processing) {
  self->setProcessingLayoutWidget(processing);
}

//  bool QFormBuilderExtra::processingLayoutWidget() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QFormBuilderExtra22processingLayoutWidgetEv(
    const QFormBuilderExtra *self) {
  return self->processingLayoutWidget();
}

//  void QFormBuilderExtra::setResourceBuilder(QResourceBuilder *builder)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFormBuilderExtra18setResourceBuilderEP16QResourceBuilder(
    QFormBuilderExtra *self,
    QResourceBuilder *builder) {
  self->setResourceBuilder(builder);
}

//  QResourceBuilder *QFormBuilderExtra::resourceBuilder() const
extern "C" Q_DECL_EXPORT
QResourceBuilder *ritual_ZNK17QFormBuilderExtra15resourceBuilderEv(
    const QFormBuilderExtra *self) {
  return self->resourceBuilder();
}

//  void QFormBuilderExtra::setTextBuilder(QTextBuilder *builder)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFormBuilderExtra14setTextBuilderEP12QTextBuilder(
    QFormBuilderExtra *self,
    QTextBuilder *builder) {
  self->setTextBuilder(builder);
}

//  QTextBuilder *QFormBuilderExtra::textBuilder() const
extern "C" Q_DECL_EXPORT
QTextBuilder *ritual_ZNK17QFormBuilderExtra11textBuilderEv(
    const QFormBuilderExtra *self) {
  return self->textBuilder();
}

//  void QFormBuilderExtra::storeCustomWidgetData(const QString &className,
//      const DomCustomWidget *d)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFormBuilderExtra21storeCustomWidgetDataERK7QStringPK15DomCustomWidget(
    QFormBuilderExtra *self,
    const QString *className,
    const DomCustomWidget *d) {
  self->storeCustomWidgetData(*className, d);
}

//  QString QFormBuilderExtra::customWidgetAddPageMethod(const QString
//      &className) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QFormBuilderExtra25customWidgetAddPageMethodERK7QString(
    const QFormBuilderExtra *self,
    const QString *className) {
  return new QString(self->customWidgetAddPageMethod(*className));
}

//  QString QFormBuilderExtra::customWidgetBaseClass(const QString
//      &className) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QFormBuilderExtra21customWidgetBaseClassERK7QString(
    const QFormBuilderExtra *self,
    const QString *className) {
  return new QString(self->customWidgetBaseClass(*className));
}

//  bool QFormBuilderExtra::isCustomWidgetContainer(const QString &className)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QFormBuilderExtra23isCustomWidgetContainerERK7QString(
    const QFormBuilderExtra *self,
    const QString *className) {
  return self->isCustomWidgetContainer(*className);
}

//  void QFormBuilderExtra::registerButtonGroups(const DomButtonGroups
//      *groups)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFormBuilderExtra20registerButtonGroupsEPK15DomButtonGroups(
    QFormBuilderExtra *self,
    const DomButtonGroups *groups) {
  self->registerButtonGroups(groups);
}

//  void QFormBuilderExtra::getLayoutMargins(const QList<DomProperty *>
//      &properties, int *left, int *top, int *right, int *bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFormBuilderExtra16getLayoutMarginsERK5QListIP11DomPropertyEPiS6_S6_S6_(
    const QList<DomProperty *> *properties,
    int *left,
    int *top,
    int *right,
    int *bottom) {
  QFormBuilderExtra::getLayoutMargins(*properties, left, top, right, bottom);
}

//  QString QFormBuilderExtra::boxLayoutStretch(const QBoxLayout *a0)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QFormBuilderExtra16boxLayoutStretchEPK10QBoxLayout(
    const QBoxLayout *a0) {
  return new QString(QFormBuilderExtra::boxLayoutStretch(a0));
}

//  bool QFormBuilderExtra::setBoxLayoutStretch(const QString &a0, QBoxLayout
//      *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QFormBuilderExtra19setBoxLayoutStretchERK7QStringP10QBoxLayout(
    const QString *a0,
    QBoxLayout *a1) {
  return QFormBuilderExtra::setBoxLayoutStretch(*a0, a1);
}

//  void QFormBuilderExtra::clearBoxLayoutStretch(QBoxLayout *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFormBuilderExtra21clearBoxLayoutStretchEP10QBoxLayout(
    QBoxLayout *a0) {
  QFormBuilderExtra::clearBoxLayoutStretch(a0);
}

//  QString QFormBuilderExtra::gridLayoutRowStretch(const QGridLayout *a0)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QFormBuilderExtra20gridLayoutRowStretchEPK11QGridLayout(
    const QGridLayout *a0) {
  return new QString(QFormBuilderExtra::gridLayoutRowStretch(a0));
}

//  bool QFormBuilderExtra::setGridLayoutRowStretch(const QString &a0,
//      QGridLayout *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QFormBuilderExtra23setGridLayoutRowStretchERK7QStringP11QGridLayout(
    const QString *a0,
    QGridLayout *a1) {
  return QFormBuilderExtra::setGridLayoutRowStretch(*a0, a1);
}

//  void QFormBuilderExtra::clearGridLayoutRowStretch(QGridLayout *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFormBuilderExtra25clearGridLayoutRowStretchEP11QGridLayout(
    QGridLayout *a0) {
  QFormBuilderExtra::clearGridLayoutRowStretch(a0);
}

//  QString QFormBuilderExtra::gridLayoutColumnStretch(const QGridLayout *a0)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QFormBuilderExtra23gridLayoutColumnStretchEPK11QGridLayout(
    const QGridLayout *a0) {
  return new QString(QFormBuilderExtra::gridLayoutColumnStretch(a0));
}

//  bool QFormBuilderExtra::setGridLayoutColumnStretch(const QString &a0,
//      QGridLayout *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QFormBuilderExtra26setGridLayoutColumnStretchERK7QStringP11QGridLayout(
    const QString *a0,
    QGridLayout *a1) {
  return QFormBuilderExtra::setGridLayoutColumnStretch(*a0, a1);
}

//  void QFormBuilderExtra::clearGridLayoutColumnStretch(QGridLayout *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFormBuilderExtra28clearGridLayoutColumnStretchEP11QGridLayout(
    QGridLayout *a0) {
  QFormBuilderExtra::clearGridLayoutColumnStretch(a0);
}

//  QString QFormBuilderExtra::gridLayoutRowMinimumHeight(const QGridLayout
//      *a0)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QFormBuilderExtra26gridLayoutRowMinimumHeightEPK11QGridLayout(
    const QGridLayout *a0) {
  return new QString(QFormBuilderExtra::gridLayoutRowMinimumHeight(a0));
}

//  bool QFormBuilderExtra::setGridLayoutRowMinimumHeight(const QString &a0,
//      QGridLayout *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QFormBuilderExtra29setGridLayoutRowMinimumHeightERK7QStringP11QGridLayout(
    const QString *a0,
    QGridLayout *a1) {
  return QFormBuilderExtra::setGridLayoutRowMinimumHeight(*a0, a1);
}

//  void QFormBuilderExtra::clearGridLayoutRowMinimumHeight(QGridLayout *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFormBuilderExtra31clearGridLayoutRowMinimumHeightEP11QGridLayout(
    QGridLayout *a0) {
  QFormBuilderExtra::clearGridLayoutRowMinimumHeight(a0);
}

//  QString QFormBuilderExtra::gridLayoutColumnMinimumWidth(const QGridLayout
//      *a0)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QFormBuilderExtra28gridLayoutColumnMinimumWidthEPK11QGridLayout(
    const QGridLayout *a0) {
  return new QString(QFormBuilderExtra::gridLayoutColumnMinimumWidth(a0));
}

//  bool QFormBuilderExtra::setGridLayoutColumnMinimumWidth(const QString
//      &a0, QGridLayout *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QFormBuilderExtra31setGridLayoutColumnMinimumWidthERK7QStringP11QGridLayout(
    const QString *a0,
    QGridLayout *a1) {
  return QFormBuilderExtra::setGridLayoutColumnMinimumWidth(*a0, a1);
}

//  void QFormBuilderExtra::clearGridLayoutColumnMinimumWidth(QGridLayout
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFormBuilderExtra33clearGridLayoutColumnMinimumWidthEP11QGridLayout(
    QGridLayout *a0) {
  QFormBuilderExtra::clearGridLayoutColumnMinimumWidth(a0);
}

//  QPalette QFormBuilderExtra::loadPalette(const DomPalette *dom)
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZN17QFormBuilderExtra11loadPaletteEPK10DomPalette(
    const DomPalette *dom) {
  return new QPalette(QFormBuilderExtra::loadPalette(dom));
}

//  void QFormBuilderExtra::setupColorGroup(QPalette *palette,
//      QPalette::ColorGroup colorGroup, const DomColorGroup *group)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFormBuilderExtra15setupColorGroupEP8QPaletteNS0_10ColorGroupEPK13DomColorGroup(
    QPalette *palette,
    QPalette::ColorGroup colorGroup,
    const DomColorGroup *group) {
  QFormBuilderExtra::setupColorGroup(palette, colorGroup, group);
}

//  DomColorGroup *QFormBuilderExtra::saveColorGroup(const QPalette &palette,
//      QPalette::ColorGroup colorGroup)
extern "C" Q_DECL_EXPORT
DomColorGroup *ritual_ZN17QFormBuilderExtra14saveColorGroupERK8QPaletteNS0_10ColorGroupE(
    const QPalette *palette,
    QPalette::ColorGroup colorGroup) {
  return QFormBuilderExtra::saveColorGroup(*palette, colorGroup);
}

//  DomPalette *QFormBuilderExtra::savePalette(const QPalette &palette)
extern "C" Q_DECL_EXPORT
DomPalette *ritual_ZN17QFormBuilderExtra11savePaletteERK8QPalette(
    const QPalette *palette) {
  return QFormBuilderExtra::savePalette(*palette);
}

//  QBrush QFormBuilderExtra::setupBrush(const DomBrush *brush)
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN17QFormBuilderExtra10setupBrushEPK8DomBrush(
    const DomBrush *brush) {
  return new QBrush(QFormBuilderExtra::setupBrush(brush));
}

//  DomBrush *QFormBuilderExtra::saveBrush(const QBrush &br)
extern "C" Q_DECL_EXPORT
DomBrush *ritual_ZN17QFormBuilderExtra9saveBrushERK6QBrush(
    const QBrush *br) {
  return QFormBuilderExtra::saveBrush(*br);
}

//  DomProperty *QFormBuilderExtra::propertyByName(const QList<DomProperty *>
//      &properties, QAnyStringView needle)
extern "C" Q_DECL_EXPORT
DomProperty *ritual_ZN17QFormBuilderExtra14propertyByNameERK5QListIP11DomPropertyE14QAnyStringView(
    const QList<DomProperty *> *properties,
    const QString *needle) {
  return QFormBuilderExtra::propertyByName(
      *properties,
      QAnyStringView(*needle));
}

//  bool QFormBuilderExtra::isQFontComboBox(const QWidget *w)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QFormBuilderExtra15isQFontComboBoxEPK7QWidget(
    const QWidget *w) {
  return QFormBuilderExtra::isQFontComboBox(w);
}

//  void QFormBuilderExtra::clearResourceBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFormBuilderExtra20clearResourceBuilderEv(
    QFormBuilderExtra *self) {
  self->clearResourceBuilder();
}

//  void QFormBuilderExtra::clearTextBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFormBuilderExtra16clearTextBuilderEv(
    QFormBuilderExtra *self) {
  self->clearTextBuilder();
}
