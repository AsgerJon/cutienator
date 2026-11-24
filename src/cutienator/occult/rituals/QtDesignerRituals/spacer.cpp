//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/spacer_widget_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/spacer_widget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  Only a class built on Spacer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnSpacer : Spacer {
  using Spacer::paintEvent;
  using Spacer::resizeEvent;
};

//  const QMetaObject *Spacer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK6Spacer10metaObjectEv(const Spacer *self) {
  return self->metaObject();
}

//  QString Spacer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6Spacer2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(Spacer::tr(s, c, n));
}

//  Spacer::Spacer(QWidget *parent)
extern "C" Q_DECL_EXPORT
Spacer *ritual_ZN6SpacerC1EP7QWidget(QWidget *parent) {
  return new Spacer(parent);
}

//  QSize Spacer::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK6Spacer8sizeHintEv(const Spacer *self) {
  return new QSize(self->sizeHint());
}

//  QSize Spacer::sizeHintProperty() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK6Spacer16sizeHintPropertyEv(const Spacer *self) {
  return new QSize(self->sizeHintProperty());
}

//  void Spacer::setSizeHintProperty(const QSize &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN6Spacer19setSizeHintPropertyERK5QSize(
    Spacer *self,
    const QSize *s) {
  self->setSizeHintProperty(*s);
}

//  QSizePolicy::Policy Spacer::sizeType() const
extern "C" Q_DECL_EXPORT
QSizePolicy::Policy ritual_ZNK6Spacer8sizeTypeEv(const Spacer *self) {
  return self->sizeType();
}

//  void Spacer::setSizeType(QSizePolicy::Policy t)
extern "C" Q_DECL_EXPORT
void ritual_ZN6Spacer11setSizeTypeEN11QSizePolicy6PolicyE(
    Spacer *self,
    QSizePolicy::Policy t) {
  self->setSizeType(t);
}

//  Qt::Alignment Spacer::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6Spacer9alignmentEv(const Spacer *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  Qt::Orientation Spacer::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK6Spacer11orientationEv(const Spacer *self) {
  return self->orientation();
}

//  void Spacer::setOrientation(Qt::Orientation o)
extern "C" Q_DECL_EXPORT
void ritual_ZN6Spacer14setOrientationEN2Qt11OrientationE(
    Spacer *self,
    Qt::Orientation o) {
  self->setOrientation(o);
}

//  void Spacer::setInteractiveMode(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN6Spacer18setInteractiveModeEb(Spacer *self, bool b) {
  self->setInteractiveMode(b);
}

//  bool Spacer::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6Spacer5eventEP6QEvent(Spacer *self, QEvent *e) {
  return self->event(e);
}

//  void Spacer::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN6Spacer10paintEventEP11QPaintEvent(
    Spacer *self,
    QPaintEvent *e) {
  self->paintEvent(e);
}

//  void Spacer::resizeEvent(QResizeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN6Spacer11resizeEventEP12QResizeEvent(
    Spacer *self,
    QResizeEvent *e) {
  self->resizeEvent(e);
}

//  void Spacer::updateMask()
extern "C" Q_DECL_EXPORT
void ritual_ZN6Spacer10updateMaskEv(Spacer *self) {
  self->updateMask();
}

//  bool Spacer::isInLayout() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6Spacer10isInLayoutEv(const Spacer *self) {
  return self->isInLayout();
}

//  void Spacer::updateToolTip()
extern "C" Q_DECL_EXPORT
void ritual_ZN6Spacer13updateToolTipEv(Spacer *self) {
  self->updateToolTip();
}

//  QSize Spacer::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK6Spacer8sizeHintEv(const Spacer *self) {
  return new QSize(self->Spacer::sizeHint());
}

//  bool Spacer::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6Spacer5eventEP6QEvent(Spacer *self, QEvent *e) {
  return self->Spacer::event(e);
}

//  void Spacer::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6Spacer10paintEventEP11QPaintEvent(
    Spacer *self,
    QPaintEvent *e) {
  static_cast<OwnSpacer *>(self)->OwnSpacer::paintEvent(e);
}

//  void Spacer::resizeEvent(QResizeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6Spacer11resizeEventEP12QResizeEvent(
    Spacer *self,
    QResizeEvent *e) {
  static_cast<OwnSpacer *>(self)->OwnSpacer::resizeEvent(e);
}
