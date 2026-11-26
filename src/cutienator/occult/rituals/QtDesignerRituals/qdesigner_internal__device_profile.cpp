//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/deviceprofile_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/deviceprofile_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  qdesigner_internal::DeviceProfile::DeviceProfile()
extern "C" Q_DECL_EXPORT
qdesigner_internal::DeviceProfile *ritual_ZN18qdesigner_internal13DeviceProfileC1Ev() {
  return new qdesigner_internal::DeviceProfile();
}

//  qdesigner_internal::DeviceProfile::DeviceProfile(const DeviceProfile &a0)
extern "C" Q_DECL_EXPORT
qdesigner_internal::DeviceProfile *ritual_ZN18qdesigner_internal13DeviceProfileC1ERKS0_(
    const qdesigner_internal::DeviceProfile *a0) {
  return new qdesigner_internal::DeviceProfile(*a0);
}

//  DeviceProfile &qdesigner_internal::DeviceProfile::operator=(const
//      DeviceProfile &a0)
extern "C" Q_DECL_EXPORT
qdesigner_internal::DeviceProfile *ritual_ZN18qdesigner_internal13DeviceProfileaSERKS0_(
    qdesigner_internal::DeviceProfile *self,
    const qdesigner_internal::DeviceProfile *a0) {
  return &(self->operator=(*a0));
}

//  qdesigner_internal::DeviceProfile::~DeviceProfile()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal13DeviceProfileD1Ev(
    qdesigner_internal::DeviceProfile *self) {
  delete self;
}

//  void qdesigner_internal::DeviceProfile::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal13DeviceProfile5clearEv(
    qdesigner_internal::DeviceProfile *self) {
  self->clear();
}

//  QString qdesigner_internal::DeviceProfile::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal13DeviceProfile4nameEv(
    const qdesigner_internal::DeviceProfile *self) {
  return new QString(self->name());
}

//  void qdesigner_internal::DeviceProfile::setName(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal13DeviceProfile7setNameERK7QString(
    qdesigner_internal::DeviceProfile *self,
    const QString *a0) {
  self->setName(*a0);
}

//  bool qdesigner_internal::DeviceProfile::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal13DeviceProfile7isEmptyEv(
    const qdesigner_internal::DeviceProfile *self) {
  return self->isEmpty();
}

//  QString qdesigner_internal::DeviceProfile::fontFamily() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal13DeviceProfile10fontFamilyEv(
    const qdesigner_internal::DeviceProfile *self) {
  return new QString(self->fontFamily());
}

//  void qdesigner_internal::DeviceProfile::setFontFamily(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal13DeviceProfile13setFontFamilyERK7QString(
    qdesigner_internal::DeviceProfile *self,
    const QString *a0) {
  self->setFontFamily(*a0);
}

//  int qdesigner_internal::DeviceProfile::fontPointSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal13DeviceProfile13fontPointSizeEv(
    const qdesigner_internal::DeviceProfile *self) {
  return self->fontPointSize();
}

//  void qdesigner_internal::DeviceProfile::setFontPointSize(int p)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal13DeviceProfile16setFontPointSizeEi(
    qdesigner_internal::DeviceProfile *self,
    int p) {
  self->setFontPointSize(p);
}

//  int qdesigner_internal::DeviceProfile::dpiX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal13DeviceProfile4dpiXEv(
    const qdesigner_internal::DeviceProfile *self) {
  return self->dpiX();
}

//  void qdesigner_internal::DeviceProfile::setDpiX(int d)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal13DeviceProfile7setDpiXEi(
    qdesigner_internal::DeviceProfile *self,
    int d) {
  self->setDpiX(d);
}

//  int qdesigner_internal::DeviceProfile::dpiY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal13DeviceProfile4dpiYEv(
    const qdesigner_internal::DeviceProfile *self) {
  return self->dpiY();
}

//  void qdesigner_internal::DeviceProfile::setDpiY(int d)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal13DeviceProfile7setDpiYEi(
    qdesigner_internal::DeviceProfile *self,
    int d) {
  self->setDpiY(d);
}

//  QString qdesigner_internal::DeviceProfile::style() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal13DeviceProfile5styleEv(
    const qdesigner_internal::DeviceProfile *self) {
  return new QString(self->style());
}

//  void qdesigner_internal::DeviceProfile::setStyle(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal13DeviceProfile8setStyleERK7QString(
    qdesigner_internal::DeviceProfile *self,
    const QString *a0) {
  self->setStyle(*a0);
}

//  void qdesigner_internal::DeviceProfile::fromSystem()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal13DeviceProfile10fromSystemEv(
    qdesigner_internal::DeviceProfile *self) {
  self->fromSystem();
}

//  void qdesigner_internal::DeviceProfile::systemResolution(int *dpiX, int
//      *dpiY)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal13DeviceProfile16systemResolutionEPiS1_(
    int *dpiX,
    int *dpiY) {
  qdesigner_internal::DeviceProfile::systemResolution(dpiX, dpiY);
}

//  void qdesigner_internal::DeviceProfile::widgetResolution(const QWidget
//      *w, int *dpiX, int *dpiY)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal13DeviceProfile16widgetResolutionEPK7QWidgetPiS4_(
    const QWidget *w,
    int *dpiX,
    int *dpiY) {
  qdesigner_internal::DeviceProfile::widgetResolution(w, dpiX, dpiY);
}

//  void qdesigner_internal::DeviceProfile::apply(const
//      QDesignerFormEditorInterface *core, QWidget *widget, ApplyMode am)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18qdesigner_internal13DeviceProfile5applyEPK28QDesignerFormEditorInterfaceP7QWidgetNS0_9ApplyModeE(
    const qdesigner_internal::DeviceProfile *self,
    const QDesignerFormEditorInterface *core,
    QWidget *widget,
    qdesigner_internal::DeviceProfile::ApplyMode am) {
  self->apply(core, widget, am);
}

//  void qdesigner_internal::DeviceProfile::applyDPI(int dpiX, int dpiY,
//      QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal13DeviceProfile8applyDPIEiiP7QWidget(
    int dpiX,
    int dpiY,
    QWidget *widget) {
  qdesigner_internal::DeviceProfile::applyDPI(dpiX, dpiY, widget);
}

//  QString qdesigner_internal::DeviceProfile::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal13DeviceProfile8toStringEv(
    const qdesigner_internal::DeviceProfile *self) {
  return new QString(self->toString());
}

//  QString qdesigner_internal::DeviceProfile::toXml() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal13DeviceProfile5toXmlEv(
    const qdesigner_internal::DeviceProfile *self) {
  return new QString(self->toXml());
}

//  bool qdesigner_internal::DeviceProfile::fromXml(const QString &xml,
//      QString *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal13DeviceProfile7fromXmlERK7QStringPS1_(
    qdesigner_internal::DeviceProfile *self,
    const QString *xml,
    QString *errorMessage) {
  return self->fromXml(*xml, errorMessage);
}

//  bool operator==(const DeviceProfile &lhs, const DeviceProfile &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_13DeviceProfileES2_(
    const qdesigner_internal::DeviceProfile *lhs,
    const qdesigner_internal::DeviceProfile *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const DeviceProfile &lhs, const DeviceProfile &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_13DeviceProfileES2_(
    const qdesigner_internal::DeviceProfile *lhs,
    const qdesigner_internal::DeviceProfile *rhs) {
  return operator!=(*lhs, *rhs);
}
