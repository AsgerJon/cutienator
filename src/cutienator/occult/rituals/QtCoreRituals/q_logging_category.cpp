//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qloggingcategory.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qloggingcategory.h>
#include <QtCore/qstring.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qloggingcategory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QLoggingCategory>

//  QLoggingCategory::QLoggingCategory(const char *category, QtMsgType
//      severityLevel)
extern "C" Q_DECL_EXPORT
QLoggingCategory *ritual_ZN16QLoggingCategoryC1EPKc9QtMsgType(
    const char *category,
    QtMsgType severityLevel) {
  return new QLoggingCategory(category, severityLevel);
}

//  QLoggingCategory::~QLoggingCategory()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLoggingCategoryD1Ev(QLoggingCategory *self) {
  delete self;
}

//  bool QLoggingCategory::isEnabled(QtMsgType type) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QLoggingCategory9isEnabledE9QtMsgType(
    const QLoggingCategory *self,
    QtMsgType type) {
  return self->isEnabled(type);
}

//  void QLoggingCategory::setEnabled(QtMsgType type, bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLoggingCategory10setEnabledE9QtMsgTypeb(
    QLoggingCategory *self,
    QtMsgType type,
    bool enable) {
  self->setEnabled(type, enable);
}

//  bool QLoggingCategory::isDebugEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QLoggingCategory14isDebugEnabledEv(
    const QLoggingCategory *self) {
  return self->isDebugEnabled();
}

//  bool QLoggingCategory::isInfoEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QLoggingCategory13isInfoEnabledEv(
    const QLoggingCategory *self) {
  return self->isInfoEnabled();
}

//  bool QLoggingCategory::isWarningEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QLoggingCategory16isWarningEnabledEv(
    const QLoggingCategory *self) {
  return self->isWarningEnabled();
}

//  bool QLoggingCategory::isCriticalEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QLoggingCategory17isCriticalEnabledEv(
    const QLoggingCategory *self) {
  return self->isCriticalEnabled();
}

//  const char *QLoggingCategory::categoryName() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK16QLoggingCategory12categoryNameEv(
    const QLoggingCategory *self) {
  return self->categoryName();
}

//  QLoggingCategory &QLoggingCategory::operator()()
extern "C" Q_DECL_EXPORT
QLoggingCategory *ritual_ZN16QLoggingCategoryclEv(QLoggingCategory *self) {
  return &(self->operator()());
}

//  const QLoggingCategory &QLoggingCategory::operator()() const
extern "C" Q_DECL_EXPORT
const QLoggingCategory *ritual_ZNK16QLoggingCategoryclEv(
    const QLoggingCategory *self) {
  return &(self->operator()());
}

//  QLoggingCategory *QLoggingCategory::defaultCategory()
extern "C" Q_DECL_EXPORT
QLoggingCategory *ritual_ZN16QLoggingCategory15defaultCategoryEv() {
  return QLoggingCategory::defaultCategory();
}

//  CategoryFilter QLoggingCategory::installFilter(CategoryFilter a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QLoggingCategory13installFilterEPFvPS_E(void *a0) {
  return reinterpret_cast<void *>(
      QLoggingCategory::installFilter(
          reinterpret_cast<QLoggingCategory::CategoryFilter>(a0)));
}

//  void QLoggingCategory::setFilterRules(const QString &rules)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLoggingCategory14setFilterRulesERK7QString(
    const QString *rules) {
  QLoggingCategory::setFilterRules(*rules);
}

//  QLoggingCategory::QLoggingCategory(UnregisteredInitialization a0, const
//      char *category)
extern "C" Q_DECL_EXPORT
QLoggingCategory *ritual_ZN16QLoggingCategoryC1ENS_26UnregisteredInitializationEPKc(
    const QLoggingCategory::UnregisteredInitialization *a0,
    const char *category) {
  return new QLoggingCategory(*a0, category);
}
