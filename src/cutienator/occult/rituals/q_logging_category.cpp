//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qloggingcategory.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qloggingcategory.h>
#include <QtCore/qstring.h>

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

//  QLoggingCategory *QLoggingCategory::defaultCategory()
extern "C" Q_DECL_EXPORT
QLoggingCategory *ritual_ZN16QLoggingCategory15defaultCategoryEv() {
  return QLoggingCategory::defaultCategory();
}

//  void QLoggingCategory::setFilterRules(const QString &rules)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLoggingCategory14setFilterRulesERK7QString(
    const QString *rules) {
  QLoggingCategory::setFilterRules(*rules);
}
