//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qhttp2configuration.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(http)
#if QT_CONFIG(http)
#include <QtNetwork/qhttp2configuration.h>

//  QHttp2Configuration::QHttp2Configuration()
extern "C" Q_DECL_EXPORT
QHttp2Configuration *ritual_ZN19QHttp2ConfigurationC1Ev() {
  return new QHttp2Configuration();
}

//  QHttp2Configuration::QHttp2Configuration(const QHttp2Configuration
//      &other)
extern "C" Q_DECL_EXPORT
QHttp2Configuration *ritual_ZN19QHttp2ConfigurationC1ERKS_(
    const QHttp2Configuration *other) {
  return new QHttp2Configuration(*other);
}

//  QHttp2Configuration::~QHttp2Configuration()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttp2ConfigurationD1Ev(QHttp2Configuration *self) {
  delete self;
}

//  void QHttp2Configuration::setServerPushEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttp2Configuration20setServerPushEnabledEb(
    QHttp2Configuration *self,
    bool enable) {
  self->setServerPushEnabled(enable);
}

//  bool QHttp2Configuration::serverPushEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QHttp2Configuration17serverPushEnabledEv(
    const QHttp2Configuration *self) {
  return self->serverPushEnabled();
}

//  void QHttp2Configuration::setHuffmanCompressionEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttp2Configuration28setHuffmanCompressionEnabledEb(
    QHttp2Configuration *self,
    bool enable) {
  self->setHuffmanCompressionEnabled(enable);
}

//  bool QHttp2Configuration::huffmanCompressionEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QHttp2Configuration25huffmanCompressionEnabledEv(
    const QHttp2Configuration *self) {
  return self->huffmanCompressionEnabled();
}

//  bool QHttp2Configuration::setSessionReceiveWindowSize(unsigned int size)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QHttp2Configuration27setSessionReceiveWindowSizeEj(
    QHttp2Configuration *self,
    unsigned int size) {
  return self->setSessionReceiveWindowSize(size);
}

//  unsigned int QHttp2Configuration::sessionReceiveWindowSize() const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK19QHttp2Configuration24sessionReceiveWindowSizeEv(
    const QHttp2Configuration *self) {
  return self->sessionReceiveWindowSize();
}

//  bool QHttp2Configuration::setStreamReceiveWindowSize(unsigned int size)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QHttp2Configuration26setStreamReceiveWindowSizeEj(
    QHttp2Configuration *self,
    unsigned int size) {
  return self->setStreamReceiveWindowSize(size);
}

//  unsigned int QHttp2Configuration::streamReceiveWindowSize() const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK19QHttp2Configuration23streamReceiveWindowSizeEv(
    const QHttp2Configuration *self) {
  return self->streamReceiveWindowSize();
}

//  bool QHttp2Configuration::setMaxFrameSize(unsigned int size)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QHttp2Configuration15setMaxFrameSizeEj(
    QHttp2Configuration *self,
    unsigned int size) {
  return self->setMaxFrameSize(size);
}

//  unsigned int QHttp2Configuration::maxFrameSize() const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK19QHttp2Configuration12maxFrameSizeEv(
    const QHttp2Configuration *self) {
  return self->maxFrameSize();
}

//  void QHttp2Configuration::setMaxConcurrentStreams(unsigned int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttp2Configuration23setMaxConcurrentStreamsEj(
    QHttp2Configuration *self,
    unsigned int value) {
  self->setMaxConcurrentStreams(value);
}

//  unsigned int QHttp2Configuration::maxConcurrentStreams() const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK19QHttp2Configuration20maxConcurrentStreamsEv(
    const QHttp2Configuration *self) {
  return self->maxConcurrentStreams();
}

//  bool QHttp2Configuration::isEqual(const QHttp2Configuration &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QHttp2Configuration7isEqualERKS_(
    const QHttp2Configuration *self,
    const QHttp2Configuration *other) {
  return self->isEqual(*other);
}

//  bool operator==(const QHttp2Configuration &lhs, const QHttp2Configuration
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK19QHttp2ConfigurationS1_(
    const QHttp2Configuration *lhs,
    const QHttp2Configuration *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QHttp2Configuration &lhs, const QHttp2Configuration
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK19QHttp2ConfigurationS1_(
    const QHttp2Configuration *lhs,
    const QHttp2Configuration *rhs) {
  return operator!=(*lhs, *rhs);
}

#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(http)
