//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qwindowsresampler_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again.
//  A 'size_t' and a 'quint64' are passed as numbers. Not written:
//  'setStartTimeOffset', taking a 'std::chrono::microseconds'; 'resample'
//  taking a 'ComPtr<IMFSample>', a template of Windows, or a 'QSpan' and
//  giving a 'std::pmr::vector'; and the private 'processOutput', a template
//  or giving a 'q23::expected'.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qwindowsresampler_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>
#include <QtMultimedia/qaudiobuffer.h>
#include <QtMultimedia/qaudioformat.h>
#include <cstring>

//  A QWindowsResampler that Python can take functions over in. Every
//  QWindowsResampler Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef const QAudioBuffer * (*CuteQWindowsResamplerCall0)(const void *, const char *, size_t, int *);
class CuteQWindowsResampler : public QWindowsResampler {
public:
  using QWindowsResampler::QWindowsResampler;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QPlatformAudioResampler8resampleEPKcy")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QAudioBuffer QWindowsResampler::resample(const char *data, size_t size)
  QAudioBuffer resample(const char *data, size_t size) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowsResamplerCall0 call = reinterpret_cast<CuteQWindowsResamplerCall0>(taken[0]);
      const QAudioBuffer * given = call(this, data, size, &handled);
      if (handled && given) return *given;
    }
    return QWindowsResampler::resample(data, size);
  }
};

//  QWindowsResampler::QWindowsResampler()
extern "C" Q_DECL_EXPORT
QWindowsResampler *ritual_ZN17QWindowsResamplerC1Ev() {
  return new CuteQWindowsResampler();
}

//  QWindowsResampler::~QWindowsResampler()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWindowsResamplerD1Ev(QWindowsResampler *self) {
  delete self;
}

//  bool QWindowsResampler::isAvailable()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QWindowsResampler11isAvailableEv() {
  return QWindowsResampler::isAvailable();
}

//  bool QWindowsResampler::setup(const QAudioFormat &in, const QAudioFormat
//      &out)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QWindowsResampler5setupERK12QAudioFormatS2_(
    QWindowsResampler *self,
    const QAudioFormat *in,
    const QAudioFormat *out) {
  return self->setup(*in, *out);
}

//  QByteArray QWindowsResampler::resample(QByteArray a0)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN17QWindowsResampler8resampleE10QByteArray(
    QWindowsResampler *self,
    const QByteArray *a0) {
  return new QByteArray(self->resample(*a0));
}

//  QByteArray QWindowsResampler::resample(const QByteArrayView &a0)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN17QWindowsResampler8resampleERK14QByteArrayView(
    QWindowsResampler *self,
    const QByteArrayView *a0) {
  return new QByteArray(self->resample(*a0));
}

//  QAudioBuffer QWindowsResampler::resample(const char *data, size_t size)
extern "C" Q_DECL_EXPORT
QAudioBuffer *ritual_ZN17QWindowsResampler8resampleEPKcy(
    QWindowsResampler *self,
    const char *data,
    size_t size) {
  return new QAudioBuffer(self->resample(data, size));
}

//  QAudioFormat QWindowsResampler::inputFormat() const
extern "C" Q_DECL_EXPORT
QAudioFormat *ritual_ZNK17QWindowsResampler11inputFormatEv(
    const QWindowsResampler *self) {
  return new QAudioFormat(self->inputFormat());
}

//  QAudioFormat QWindowsResampler::outputFormat() const
extern "C" Q_DECL_EXPORT
QAudioFormat *ritual_ZNK17QWindowsResampler12outputFormatEv(
    const QWindowsResampler *self) {
  return new QAudioFormat(self->outputFormat());
}

//  quint64 QWindowsResampler::outputBufferSize(quint64 inputBufferSize)
//      const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK17QWindowsResampler16outputBufferSizeEy(
    const QWindowsResampler *self,
    quint64 inputBufferSize) {
  return self->outputBufferSize(inputBufferSize);
}

//  quint64 QWindowsResampler::inputBufferSize(quint64 outputBufferSize)
//      const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK17QWindowsResampler15inputBufferSizeEy(
    const QWindowsResampler *self,
    quint64 outputBufferSize) {
  return self->inputBufferSize(outputBufferSize);
}

//  quint64 QWindowsResampler::totalInputBytes() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK17QWindowsResampler15totalInputBytesEv(
    const QWindowsResampler *self) {
  return self->totalInputBytes();
}

//  quint64 QWindowsResampler::totalOutputBytes() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK17QWindowsResampler16totalOutputBytesEv(
    const QWindowsResampler *self) {
  return self->totalOutputBytes();
}

//  qsizetype QWindowsResampler::overAllocatedOutputBufferSize()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN17QWindowsResampler29overAllocatedOutputBufferSizeEv(
    QWindowsResampler *self) {
  return self->overAllocatedOutputBufferSize();
}

//  a Python function taken by a CuteQWindowsResampler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowsResampler(
    QWindowsResampler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowsResampler *>(self)->take(key, call);
}

//  QAudioBuffer QWindowsResampler::resample(const char *data, size_t size)
extern "C" Q_DECL_EXPORT
QAudioBuffer *ritual_own_ZN17QWindowsResampler8resampleEPKcy(
    QWindowsResampler *self,
    const char *data,
    size_t size) {
  return new QAudioBuffer(self->QWindowsResampler::resample(data, size));
}

#endif  // defined(Q_OS_WIN)
