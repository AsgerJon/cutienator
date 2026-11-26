//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/qmqtttopicfilter.h, Qt 6.12.0. Changes made here are lost.
#include <QtMqtt/qmqtttopicfilter.h>
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>
#include <QtMqtt/qmqtttopicname.h>

//  QMqttTopicFilter::QMqttTopicFilter(const QString &filter)
extern "C" Q_DECL_EXPORT
QMqttTopicFilter *ritual_ZN16QMqttTopicFilterC1ERK7QString(
    const QString *filter) {
  return new QMqttTopicFilter(*filter);
}

//  QMqttTopicFilter::QMqttTopicFilter(const QLatin1String &filter)
extern "C" Q_DECL_EXPORT
QMqttTopicFilter *ritual_ZN16QMqttTopicFilterC1ERK13QLatin1String(
    const QLatin1String *filter) {
  return new QMqttTopicFilter(*filter);
}

//  QMqttTopicFilter::QMqttTopicFilter(const QMqttTopicFilter &filter)
extern "C" Q_DECL_EXPORT
QMqttTopicFilter *ritual_ZN16QMqttTopicFilterC1ERKS_(
    const QMqttTopicFilter *filter) {
  return new QMqttTopicFilter(*filter);
}

//  QMqttTopicFilter::~QMqttTopicFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMqttTopicFilterD1Ev(QMqttTopicFilter *self) {
  delete self;
}

//  QMqttTopicFilter &QMqttTopicFilter::operator=(const QMqttTopicFilter
//      &filter)
extern "C" Q_DECL_EXPORT
QMqttTopicFilter *ritual_ZN16QMqttTopicFilteraSERKS_(
    QMqttTopicFilter *self,
    const QMqttTopicFilter *filter) {
  return &(self->operator=(*filter));
}

#if defined(Q_COMPILER_RVALUE_REFS)
//  QMqttTopicFilter &QMqttTopicFilter::operator=(QMqttTopicFilter &&other)
extern "C" Q_DECL_EXPORT
QMqttTopicFilter *ritual_ZN16QMqttTopicFilteraSEOS_(
    QMqttTopicFilter *self,
    QMqttTopicFilter *other) {
  return &(self->operator=(std::move(*other)));
}
#endif  // defined(Q_COMPILER_RVALUE_REFS)

//  void QMqttTopicFilter::swap(QMqttTopicFilter &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMqttTopicFilter4swapERS_(
    QMqttTopicFilter *self,
    QMqttTopicFilter *other) {
  self->swap(*other);
}

//  QString QMqttTopicFilter::filter() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QMqttTopicFilter6filterEv(
    const QMqttTopicFilter *self) {
  return new QString(self->filter());
}

//  void QMqttTopicFilter::setFilter(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMqttTopicFilter9setFilterERK7QString(
    QMqttTopicFilter *self,
    const QString *filter) {
  self->setFilter(*filter);
}

//  QString QMqttTopicFilter::sharedSubscriptionName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QMqttTopicFilter22sharedSubscriptionNameEv(
    const QMqttTopicFilter *self) {
  return new QString(self->sharedSubscriptionName());
}

//  bool QMqttTopicFilter::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMqttTopicFilter7isValidEv(const QMqttTopicFilter *self) {
  return self->isValid();
}

//  bool QMqttTopicFilter::match(const QMqttTopicName &name, MatchOptions
//      matchOptions) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMqttTopicFilter5matchERK14QMqttTopicName6QFlagsINS_11MatchOptionEE(
    const QMqttTopicFilter *self,
    const QMqttTopicName *name,
    int matchOptions) {
  return self->match(
      *name,
      QFlags<QMqttTopicFilter::MatchOption>::fromInt(matchOptions));
}

//  bool operator==(const QMqttTopicFilter &lhs, const QMqttTopicFilter &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK16QMqttTopicFilterS1_(
    const QMqttTopicFilter *lhs,
    const QMqttTopicFilter *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QMqttTopicFilter &lhs, const QMqttTopicFilter &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK16QMqttTopicFilterS1_(
    const QMqttTopicFilter *lhs,
    const QMqttTopicFilter *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QMqttTopicFilter &lhs, const QMqttTopicFilter &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK16QMqttTopicFilterS1_(
    const QMqttTopicFilter *lhs,
    const QMqttTopicFilter *rhs) {
  return operator<(*lhs, *rhs);
}
