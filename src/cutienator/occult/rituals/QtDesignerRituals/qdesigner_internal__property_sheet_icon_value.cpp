//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  qdesigner_internal::PropertySheetIconValue::PropertySheetIconValue(const
//      PropertySheetPixmapValue &pixmap)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetIconValue *ritual_ZN18qdesigner_internal22PropertySheetIconValueC1ERKNS_24PropertySheetPixmapValueE(
    const qdesigner_internal::PropertySheetPixmapValue *pixmap) {
  return new qdesigner_internal::PropertySheetIconValue(*pixmap);
}

//  qdesigner_internal::PropertySheetIconValue::PropertySheetIconValue()
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetIconValue *ritual_ZN18qdesigner_internal22PropertySheetIconValueC1Ev() {
  return new qdesigner_internal::PropertySheetIconValue();
}

//  qdesigner_internal::PropertySheetIconValue::~PropertySheetIconValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22PropertySheetIconValueD1Ev(
    qdesigner_internal::PropertySheetIconValue *self) {
  delete self;
}

//  qdesigner_internal::PropertySheetIconValue::PropertySheetIconValue(const
//      PropertySheetIconValue &a0)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetIconValue *ritual_ZN18qdesigner_internal22PropertySheetIconValueC1ERKS0_(
    const qdesigner_internal::PropertySheetIconValue *a0) {
  return new qdesigner_internal::PropertySheetIconValue(*a0);
}

//  PropertySheetIconValue
//      &qdesigner_internal::PropertySheetIconValue::operator=(const
//      PropertySheetIconValue &a0)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetIconValue *ritual_ZN18qdesigner_internal22PropertySheetIconValueaSERKS0_(
    qdesigner_internal::PropertySheetIconValue *self,
    const qdesigner_internal::PropertySheetIconValue *a0) {
  return &(self->operator=(*a0));
}

//  qdesigner_internal::PropertySheetIconValue::PropertySheetIconValue(Proper
//      tySheetIconValue &&a0)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetIconValue *ritual_ZN18qdesigner_internal22PropertySheetIconValueC1EOS0_(
    qdesigner_internal::PropertySheetIconValue *a0) {
  return new qdesigner_internal::PropertySheetIconValue(std::move(*a0));
}

//  PropertySheetIconValue &qdesigner_internal::PropertySheetIconValue::opera
//      tor=(PropertySheetIconValue &&a0)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetIconValue *ritual_ZN18qdesigner_internal22PropertySheetIconValueaSEOS0_(
    qdesigner_internal::PropertySheetIconValue *self,
    qdesigner_internal::PropertySheetIconValue *a0) {
  return &(self->operator=(std::move(*a0)));
}

//  bool qdesigner_internal::PropertySheetIconValue::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal22PropertySheetIconValue7isEmptyEv(
    const qdesigner_internal::PropertySheetIconValue *self) {
  return self->isEmpty();
}

//  QString qdesigner_internal::PropertySheetIconValue::theme() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal22PropertySheetIconValue5themeEv(
    const qdesigner_internal::PropertySheetIconValue *self) {
  return new QString(self->theme());
}

//  void qdesigner_internal::PropertySheetIconValue::setTheme(const QString
//      &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22PropertySheetIconValue8setThemeERK7QString(
    qdesigner_internal::PropertySheetIconValue *self,
    const QString *a0) {
  self->setTheme(*a0);
}

//  int qdesigner_internal::PropertySheetIconValue::themeEnum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal22PropertySheetIconValue9themeEnumEv(
    const qdesigner_internal::PropertySheetIconValue *self) {
  return self->themeEnum();
}

//  void qdesigner_internal::PropertySheetIconValue::setThemeEnum(int e)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22PropertySheetIconValue12setThemeEnumEi(
    qdesigner_internal::PropertySheetIconValue *self,
    int e) {
  self->setThemeEnum(e);
}

//  PropertySheetPixmapValue
//      qdesigner_internal::PropertySheetIconValue::pixmap(QIcon::Mode mode,
//      QIcon::State state) const
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetPixmapValue *ritual_ZNK18qdesigner_internal22PropertySheetIconValue6pixmapEN5QIcon4ModeENS1_5StateE(
    const qdesigner_internal::PropertySheetIconValue *self,
    QIcon::Mode mode,
    QIcon::State state) {
  return new qdesigner_internal::PropertySheetPixmapValue(
      self->pixmap(
          mode,
          state));
}

//  void qdesigner_internal::PropertySheetIconValue::setPixmap(QIcon::Mode
//      mode, QIcon::State state, const PropertySheetPixmapValue &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22PropertySheetIconValue9setPixmapEN5QIcon4ModeENS1_5StateERKNS_24PropertySheetPixmapValueE(
    qdesigner_internal::PropertySheetIconValue *self,
    QIcon::Mode mode,
    QIcon::State state,
    const qdesigner_internal::PropertySheetPixmapValue *path) {
  self->setPixmap(mode, state, *path);
}

//  uint qdesigner_internal::PropertySheetIconValue::mask() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18qdesigner_internal22PropertySheetIconValue4maskEv(
    const qdesigner_internal::PropertySheetIconValue *self) {
  return self->mask();
}

//  uint qdesigner_internal::PropertySheetIconValue::compare(const
//      PropertySheetIconValue &other) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18qdesigner_internal22PropertySheetIconValue7compareERKS0_(
    const qdesigner_internal::PropertySheetIconValue *self,
    const qdesigner_internal::PropertySheetIconValue *other) {
  return self->compare(*other);
}

//  void qdesigner_internal::PropertySheetIconValue::assign(const
//      PropertySheetIconValue &other, uint mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22PropertySheetIconValue6assignERKS0_j(
    qdesigner_internal::PropertySheetIconValue *self,
    const qdesigner_internal::PropertySheetIconValue *other,
    uint mask) {
  self->assign(*other, mask);
}

//  PropertySheetIconValue
//      qdesigner_internal::PropertySheetIconValue::themed() const
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetIconValue *ritual_ZNK18qdesigner_internal22PropertySheetIconValue6themedEv(
    const qdesigner_internal::PropertySheetIconValue *self) {
  return new qdesigner_internal::PropertySheetIconValue(self->themed());
}

//  PropertySheetIconValue
//      qdesigner_internal::PropertySheetIconValue::unthemed() const
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetIconValue *ritual_ZNK18qdesigner_internal22PropertySheetIconValue8unthemedEv(
    const qdesigner_internal::PropertySheetIconValue *self) {
  return new qdesigner_internal::PropertySheetIconValue(self->unthemed());
}

//  const ModeStateToPixmapMap
//      &qdesigner_internal::PropertySheetIconValue::paths() const
extern "C" Q_DECL_EXPORT
const qdesigner_internal::PropertySheetIconValue::ModeStateToPixmapMap *ritual_ZNK18qdesigner_internal22PropertySheetIconValue5pathsEv(
    const qdesigner_internal::PropertySheetIconValue *self) {
  return &(self->paths());
}

//  bool operator==(const PropertySheetIconValue &lhs, const
//      PropertySheetIconValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_22PropertySheetIconValueES2_(
    const qdesigner_internal::PropertySheetIconValue *lhs,
    const qdesigner_internal::PropertySheetIconValue *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const PropertySheetIconValue &lhs, const
//      PropertySheetIconValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_22PropertySheetIconValueES2_(
    const qdesigner_internal::PropertySheetIconValue *lhs,
    const qdesigner_internal::PropertySheetIconValue *rhs) {
  return operator!=(*lhs, *rhs);
}
